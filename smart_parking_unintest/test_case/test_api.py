import json
import unittest

import ddt

from common.httpSet import HttpMethod
from common.read_data import Read


@ddt.ddt
class TestApi(unittest.TestCase):
    test_data = Read().get_data('API测试数据', "api")

    def setUp(self) -> None:
        self.method = HttpMethod()

    @ddt.data(*test_data)
    @ddt.unpack
    def test_1_api(self, id, method, url, msgtext, data, tablename, field, key):
        if method == 'get':
            head = {"Accept": "application/json, text/plain, */*",
                "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'}
            resp = self.method.method(method, url, data, headers=head)
            print(resp)
        else:
            head = {"Content-Type":"application/json"}
            js = json.loads(data)
            resp = self.method.method(method, url, data=js, headers=head)
            print(resp)
        self.assertEqual(resp['msg'], msgtext)
