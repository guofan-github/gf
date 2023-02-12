
import unittest

from pages.shebeishuxing import sbsxyewu
from pages.xunjianshenhe_yw import EmployeeBusiness
from pages.yonghuguanli_yw import yhglyewu


class xjshhCase(unittest.TestCase):

    def test_xjshh(self):
        # 类的实例化
        n = EmployeeBusiness()
        # 调用发布公告的方法
        r = n.xjshh_shenhexunjianrenwu(shhyj="你巡的是个勾八")

        # 断言
        self.assertEqual(r,'审核成功')


    def test_yhgltj(self):
        g = yhglyewu()
        c = g.yhgl_tianjiayonghu('彭于晏','pyy',13133450853,'3046pyy',)
        self.assertEqual(c,"成功")

    def test_yhglxg(self):
        q = yhglyewu()
        v = q.yhgl_xiugaiyonghuxinxi('郭凡',13353430752)
        self.assertEqual(v,'成功')

    def test_sbsxtj(self):
        sxtj = sbsxyewu()
        tjyw = sxtj.sbsx_tianjiayewu('寄','啊对对对')
        self.assertEqual(tjyw, '添加成功')

    def test_sbsxxg(self):
        sxxg = sbsxyewu()
        xgyw = sxxg.sbsx_xiugaiyewu('ji','nitaimei')
        self.assertEqual(xgyw, '修改成功')

    def test_sbsxsc(self):
        sxsc = sbsxyewu()
        scyw = sxsc.sbxz_shanchuyewu()
        self.assertEqual(scyw, '删除成功')
        