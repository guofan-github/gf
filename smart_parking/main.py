
import requests
#
# o = requests.get('http://192.168.163.131/smart_parking_bg/login/captcha')
# print(o.text)
from faker import Faker

from test.test_login_api import TestLoginApi
#
# A = {"Authorization":'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50TmFtZSI6ImdmIiwic2FsdCI6ImU0YTMzZmQ1LTcxZDUtNGQyZi1iNTY3LTVkZDk4NTQwOTQ1MSJ9.IO5EHiP0CQTGogQI8GQSxcNks3_HTM6_y8Yige9Xr-I'}
# F = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
#     'Accept':'application/json, text/plain, */*' }
# b ={"accountName":"gf","password":"vvv333","captcha":"0000","captchaKey":"0000"}
# a = requests.post('http://192.168.163.131/smart_parking_bg/login',json=b, headers=F)
# print(a.status_code)
# # print(a.text)
# print(a.json())
# print(len(a.json()["msg"]))

# a = Faker(locale='zh-CN')
# print(a.user_name())
# d = {"id":"-1","accountName":"22vv","password":"vvv333","checkPass":"vvv333","tel":"13333333333","realName":"221","haveRoleList":[2],"state":1}
#
# g = requests.post('http://192.168.163.131/smart_parking_bg/staff/insert', json=d)
#
# print(g.text)