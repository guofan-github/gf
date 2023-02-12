import os.path
import smtplib
import time
import zipfile
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pymysql
from CBT.ATM.common.logger import Log


class Report:
    def __init__(self, version):
        self.version = version
        self.current_folder = os.path.dirname(__file__)
        self.logger = Log.get_logger()

    def write_report(self, module, type, case, result, error, screenshot):
        con = pymysql.connect(user='root', password='123456',
                              host='192.168.163.131', port=3307,
                              db='woniutest', charset='utf8')

        cur = con.cursor()
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        # sql = f'insert into report(version, module, type,' \
        #       f' case_title, result, time, error, screenshot) values("{self.version}",' \
        #       f' "{module}", "{type}", "{case}", "{result}", "{now}",' \
        #       f' "{error}", "{screenshot}")'
        sql = 'insert into report(version, module, type, case_title,' \
              ' result, time, error, screenshot) values(%s, %s, %s, %s,' \
              ' %s, %s, %s, %s)'
        self.logger.info(sql)
        cur.execute(sql, (self.version, module, type, case, result, now, error, screenshot))
        con.commit()
        cur.close()
        con.close()

    def generate_report(self):
        con = pymysql.connect(user='root', password='123456',
                              host='192.168.163.131', port=3307,
                              db='woniutest', charset='utf8')

        cur = con.cursor()
        sql = f'select * from report where version = {self.version}'
        cur.execute(sql)
        result = cur.fetchall()
        if not result:
            print(f'没有找到{self.version}版本的测试报告记录')
            return

        template_path = os.path.join(self.current_folder, 'template.html')
        with open(template_path, 'r', encoding='utf8') as f:
            content = f.read()
        content = content.replace('$test_version', self.version)
        content = content.replace('$success', self.count(cur, '成功'))
        content = content.replace('$fail', self.count(cur, '失败'))
        content = content.replace('$error', self.count(cur, '错误'))

        lasttime_sql = f'select time from report where version = "{self.version}"' \
                       f' order by time desc limit 1'
        cur.execute(lasttime_sql)
        lasttime = str(cur.fetchone()[0])
        content = content.replace('$test_time', lasttime)
        content = content.replace('$test_date', lasttime.split(' ')[0])
        test_data = ''

        for index, record in enumerate(result, 1):
            if record[5] == '成功':
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
        report_path = os.path.join(os.path.dirname(self.current_folder),
                                   f'report/report_{self.version}.html')
        with open(report_path, 'w', encoding='utf8') as f:
            f.write(content)

        cur.close()
        con.close()

    def count(self, cursor, result_status):
        sql = f'select count(result) from report where' \
              f' result = "{result_status}" and version = "{self.version}"'
        cursor.execute(sql)
        return str(cursor.fetchone()[0])

    def capure_screenshot(self, driver):

        screen_path = os.path.join(os.path.dirname(self.current_folder), 'report/screenshot')
        if not os.path.exists(screen_path):
            os.makedirs(screen_path)

        screen_name = f'{self.version}_{time.time()}.png'
        screenshot = os.path.join(screen_path, screen_name)

        driver.get_screenshot_as_file(screenshot)

        return f'screenshot/{screen_name}'

    def compress_report(self):
        report_path = os.path.join(os.path.dirname(self.current_folder), 'report')
        filelist = []
        for root, folders, filenames in os.walk(report_path):
            # print('root', root)
            # print('filenames', filenames)
            # print('folders', folders)
            for filename in filenames:
                if self.version in filename and not filename.endswith('.zip'):
                    filelist.append(os.path.join(root, filename))
            for folder in folders:
                filelist.append(os.path.join(root, folder))
        filename = os.path.join(report_path, f'report_{self.version}.zip')
        zip = zipfile.ZipFile(filename, 'w', zipfile.ZIP_LZMA)
        for file in filelist:
            zip.write(file, file.split('report', 1)[1])
        zip.close()
        return filename

    def send_mail(self, attachment):
        sender = '1579749483@qq.com'
        # receicers = ['tom@woniuxy.com', 'jerry@woniuxy.com']
        receicers = ['1579749483@qq.com','481375328@qq.com','1727254353@qq.com','770252619@qq.com']
        # message = MIMEText('这是一封简单邮件', 'text', 'utf8')
        # message['Subject'] = Header('邮件标题', 'utf8')
        message = MIMEMultipart()
        message.attach(MIMEText('<p style="color:red;'
                                'font-size:30px">这是一封来自智慧水务的邮件</p>'
                                'html', 'utf8'))
        message['Subject'] = Header('我的智慧水务测试报告', 'utf8')
        with open(attachment, 'rb') as f:
            attach = MIMEApplication(f.read())
        attach.add_header('Content-Disposition', 'attachment',
                          filename=os.path.basename(attachment))
        message.attach(attach)
        mail = smtplib.SMTP_SSL('smtp.qq.com')
        try:
            mail.connect('smtp.qq.com', 465)
            mail.login('1579749483@qq.com', 'zaetvfoluohxbaef')
            mail.sendmail(sender, receicers, message.as_string())
            self.logger.info(print('邮件发送成功！'))
        except smtplib.SMTPException as e:
            self.logger.info(print(f'邮件发送失败。错误原因：{str(e)}。'))
        finally:
            mail.close()


if __name__ == '__main__':
    report = Report('0.01')
    # report.generate_report()
    attachment = report.compress_report()
    report.send_mail(attachment)
