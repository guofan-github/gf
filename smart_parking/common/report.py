import os
import smtplib
import time
import zipfile
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pymysql

from common.logger import Log


class Report:

    def __init__(self, version):
        self.version = version
        self.current_folder = os.path.dirname(__file__)

    # 写入报告至数据库
    def write_report(self, module, type, case_title, result, error, screenshot):
        # 获取数据库的连接对象
        con = pymysql.connect(user='root', password='123456',
                              host='192.168.163.131', port=3307,
                              db='woniutest', charset='utf8')
        # 获取游标对象
        cur = con.cursor()
        # 获取当前时间
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        # sql语句
        sql = 'insert into report(version, module, type, case_title, ' \
              'result, time, error, screenshot) values(%s, %s,%s, %s,' \
              '%s, %s,%s, %s)'
        # 执行sql
        cur.execute(sql, (self.version, module, type, case_title, result, now, error, screenshot))
        # 执行commit提交命令
        con.commit()
        # 清理资源
        con.close()
        cur.close()


    # 生成报告
    def generate_report(self):
        # 获取数据库的连接对象
        con = pymysql.connect(user='root', password='123456',
                              host='192.168.163.131', port=3307,
                              db='woniutest', charset='utf8')
        # 获取游标对象
        cur = con.cursor()
        # 从数据库获取当前版本的报告
        sql = f'select * from report where version = {self.version}'
        # 执行sql
        cur.execute(sql)
        # 变量接受查询到的报告结果
        result = cur.fetchall()
        # 判断返回结果是否有
        if not result:
            print(f'没有找到{self.version}版本的测试报告记录~')
            return
        # 读取测试报告的模板文件
        template_path = os.path.join(self.current_folder, 'template.html')
        with open(template_path, 'r', encoding='utf8') as f:
            content = f.read()
        # 首先修改替换真实的版本
        content = content.replace('$test_version', self.version)
        # 统计成功、失败、错误的个数
        content = content.replace('$success', self.count(cur, '成功'))
        content = content.replace('$fail', self.count(cur, '失败'))
        content = content.replace('$error', self.count(cur, '错误'))
        # 获取测试结果的时间
        lasttime_sql =f'select time from report where version = {self.version}' \
                      f'order by time desc limit 1'
        cur.execute(lasttime_sql)
        lasttime = str(cur.fetchone()[0])
        # 替换时间
        content = content.replace('$test_time', lasttime)
        content = content.replace('$test_date', lasttime.split(' ')[0])
        test_data = ''
        # 利用枚举函数，同时拿到循环的内容和序号
        for index,record in enumerate(result, 1):
            if record[5]== '成功':
                color = 'lightgreen'
            elif record[5] == '失败':
                color = 'yellow'
            else:
                color = 'red'
            if record[8] == '无':
                link_text = '无'
            else:
                link_text = f'<a href="{record[8]}">查看截图</a>'
            test_data += f'<tr height="40">' \
                         f'<td width="7%">{index}</td>' \
                         f'<td width="9%">{record[2]}</td>' \
                         f'<td width="10%">{record[3]}</td>' \
                         f'<td width="20%">{record[4]}</td>' \
                         f'<td width="7%" bgcolor="{color}">{record[5]}</td>' \
                         f'<td width="15%">{record[6]}</td>' \
                         f'<td width="15%">{record[7]}</td>' \
                         f'<td width="10%">{link_text}</td>' \
                         f'</tr>'
        content = content.replace('$test_data', test_data)
        # 将准备好的报告结果写入文件
        report_path = os.path.join(os.path.dirname(self.current_folder),
                                       f'report/report_{self.version}.html')
        with open(report_path, 'w', encoding='utf8') as f:
            f.write(content)
        # 清理数据库资源
        cur.close()
        con.close()



    # 统计查询到的版本记录中X个数
    def count(self, cursor, result_status):
        sql = f'select count(result) from report where ' \
              f'result = "{result_status}" and version = "{self.version}"'
        cursor.execute(sql)
        return str(cursor.fetchone()[0])

    # 截图
    def capture_screenshot(self, driver):
        # 构造截图保存路径
        screenshot_path = os.path.join(os.path.dirname(self.current_folder), 'report/screenshot')
        # 检查路径是否存在，不存在需要创建
        if not os.path.exists(screenshot_path):
            os.mkdir(screenshot_path)
        # 拼接截图文件名，避免重复被覆盖
        screenname = f'{self.version}_{time.time()}.png'
        screenshot = os.path.join(screenshot_path, screenname)
        # 利用selenium截图
        driver.get_screenshot_as_file(screenshot)
        # 返回截图的相对路径
        # 注意这里的/不要用\，否则数据库会报错
        return f'screenshot/{screenname}'

    # 压缩报告
    def compress_report(self):
        # report路径
        report_path = os.path.join(os.path.dirname(self.current_folder), 'report')
        filelist = []
        for root,folders,filenames in os.walk(report_path):
            for filename in filenames:
                if self.version in filename and not filename.endswith('.zip'):
                    filelist.append(os.path.join(root, filename))
            for folder in folders:
                filelist.append(os.path.join(root, folder))
        zip_file = os.path.join(report_path, f'report_{self.version}.zip')
        zip = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_LZMA)
        for file in filelist:
            zip.write(file, file.split("report", 1)[1])
        zip.close()
        return zip_file

    # 发送报告
    def send_report(self, attachment):
        sender = '1579749483@qq.com'
        receicers = ["770252619@qq.com", "1727254353@qq.com", "11065448@qq.com", "821079850@qq.com",
                     "1693829076@qq.com", "1255933049@qq.com", '1549596771@qq.com', '2044898513@qq.com',
                     "1454796158@qq.com", '991231180@qq.com', '11065748@qq.com']
        # 构造一个不用添加附件的邮件的方法
        # MIMEText有三个参数，第一个参数是邮件正文内容，可以是字符串，也可以是html代码
        # 第二个参数是邮件类型，第三个参数是字符集
        # message = MIMEText('这是一封简单邮件', 'text', 'utf8')
        # Header有二个参数，第一个参数是邮件标题内容，第二个参数是字符集
        # 注意添加邮件标题时Subject这是固定写法，单词不可变。
        # message['Subject'] = Header('邮件标题', 'utf8')
        # 构造一个带附件的邮件的方法
        # 利用MIMEMultipart获得带附件邮件的对象
        message = MIMEMultipart()
        # 添加正文邮件内容
        message.attach(MIMEText('<p style="color:green;'
                                'font-size:30px">你相信光吗QAQ</p>',
                                'html', 'utf8'))
        # 添加邮件标题
        message['Subject'] = Header('郭凡QAQ', 'utf8')
        # 读取附件，压缩包要用二进制读取
        with open(attachment, 'rb') as f:
            # 利用MIMEApplication构造邮件附件对象
            attach = MIMEApplication(f.read())
        # 为附件加上必须的头信息
        attach.add_header('Content-Disposition', 'attachment',
                          filename=os.path.basename(attachment))
        # 将附件对象加入邮件中
        message.attach(attach)
        # 发送邮件
        mail = smtplib.SMTP_SSL('smtp.qq.com')
        try:
            mail.connect('smtp.qq.com', 465)
            mail.login('1579749483@qq.com', 'flpxgxsysqbligad')
            mail.sendmail(sender, receicers, message.as_string())
            mail.quit()
            print('邮件发送成功！')
        except smtplib.SMTPException as e:
            print(f'邮件发送失败。错误原因：{str(e)}。')
        finally:
            mail.close()

