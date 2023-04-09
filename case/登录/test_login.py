import pytest
from lib.webui import loginAndCheck

class Test_mimacuowu:

    def test_ui_001(self):
        print('\n用例UI-001')
        alertText=loginAndCheck(None,'88888888')
        assert alertText=='请输入用户名'

    def test_ui_002(self):
        print('\n用例002')
        alertText=loginAndCheck('byhy',None)
        assert alertText=='请输入密码'

    def test_ui_003(self):
        print('\n用例003')
        alertText=loginAndCheck('byh','8888888')
        assert alertText=='登录失败 : 用户名或者密码错误'

    def test_ui_004(self):
        print('\n用例004')
        alertText=loginAndCheck('byhy','8888888')
        assert alertText=='登录失败 : 用户名或者密码错误'

    def test_ui_005(self):
        print('\n用例005')
        alertText=loginAndCheck('byhy','888888888')
        assert alertText=='登录失败 : 用户名或者密码错误'