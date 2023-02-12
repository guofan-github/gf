
from CBT.ATM.module.module_test_tjcgx import ModuleTjcgx
from CBT.ATM.module.module_test_shlb import ModuleShlb
from CBT.ATM.module.module_test_cgfk import ModuleCgfk
from CBT.ATM.common.report import Report
from CBT.ATM.module.module_test_bzsjxx import ModuleBzsjxx
from CBT.ATM.module.module_test_bzxx import ModuleBzxx
from CBT.ATM.module.module_zhsw_bgjk import Modulebgjk
from CBT.ATM.module.module_zhsw_jcss import Modulejcss
from CBT.ATM.module.module_zhsw_sblb import Modulesblb
from CBT.ATM.module.mudule_zhsw_sbsx import Modulesbsx
from CBT.ATM.module.module_login import ModuleLogin
from CBT.ATM.module.moudle_zhsw_wxxt import Modulewxxtwpgd
from CBT.ATM.module.module_wxxt_ypgd import Modulewxxtypgd
from CBT.ATM.module.moudle_wxxt_wshgd import ModulewxxtWSHgd
from CBT.ATM.module.moudle_wxxt_yshgd import Modulewxxtyshgd
from CBT.ATM.module.moudle_wxxt_sbwx import Modulewxxtsbwx
from CBT.ATM.module.module_zhsw_jsgl import Modulejsgl
from CBT.ATM.module.module_zhsw_xjdd import Modulexjdd
from CBT.ATM.module.module_zhsw_xjjh import Modulexjjh
from CBT.ATM.module.module_zhsw_xjsh import Modulexjsh
from CBT.ATM.module.module_zhsw_yhgl import Moduleyhgl
from CBT.ATM.module.moudle_zhsw_xjrw import Modulexjrw

TEST_VERSION = '0.02'

login = ModuleLogin(TEST_VERSION)
login.main_test()

jcss = Modulejcss(TEST_VERSION)
jcss.main_test()

sblb = Modulesblb(TEST_VERSION)
sblb.main_test()

sbsx = Modulesbsx(TEST_VERSION)
sbsx.main_test()

bgjk = Modulebgjk(TEST_VERSION)
bgjk.main_test()

tjcgx = ModuleTjcgx(TEST_VERSION)
tjcgx.main_test()
shlb = ModuleShlb(TEST_VERSION)
shlb.main_test()
cgfk = ModuleCgfk(TEST_VERSION)
cgfk.main_test()
bzxx = ModuleBzxx(TEST_VERSION)
bzxx.main_test()
bzsjxx = ModuleBzsjxx(TEST_VERSION)
bzsjxx.main_test()

wpgd = Modulewxxtwpgd(TEST_VERSION)
wpgd.main_test()

ypgd = Modulewxxtypgd(TEST_VERSION)
ypgd.main_test()

wshgd = ModulewxxtWSHgd(TEST_VERSION)
wshgd.main_test()

yshgd = Modulewxxtyshgd(TEST_VERSION)
yshgd.main_test()

sbwx = Modulewxxtsbwx(TEST_VERSION)
sbwx.main_test()

# 角色管理
jsgl = Modulejsgl(TEST_VERSION)
jsgl.main_test()

# 用户管理
yhgl = Moduleyhgl(TEST_VERSION)
yhgl.main_test()

# 巡检地点
xjdd = Modulexjdd(TEST_VERSION)
xjdd.main_test()

# 巡检任务
xjrw = Modulexjrw(TEST_VERSION)
xjrw.main_test()

# 巡检计划
xjjh = Modulexjjh(TEST_VERSION)
xjjh.main_test()

# 巡检审核
xjsh = Modulexjsh(TEST_VERSION)
xjsh.main_test()

report = Report(TEST_VERSION)
aa = report.compress_report()
report.send_mail(aa)
