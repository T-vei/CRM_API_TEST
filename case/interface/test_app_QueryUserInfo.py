#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest,requests,sys
from CRM_API_TEST.case.interface.uklRequest import loginReq,uklReq
from CRM_API_TEST.public.readConf import config,CONFIG_FILE,REPORT_PATH
from CRM_API_TEST.public.log import LOG
from CRM_API_TEST.public.common import *
from CRM_API_TEST.public.HTMLTestRunner_PY3 import HTMLTestRunner


class app_QueryUserInfo(unittest.TestCase):
    def setUp(self):
        lg = loginReq('tmlUser1')
        self.access_token = lg.get()[1]
        self.userId = lg.get()[0]
    def tearDown(self):
        pass

    def test_app_QueryUserInfo_0(self):
        '''查询用户信息'''
        data = {
            "streamNo": "UKAPP20151113161019000001",
            "partnerCode": "UKAPP",
            "loginCustomerId": self.userId,
            "needPkgFirstFlag": "false"
        }
        ur = uklReq('app_QueryUserInfo')
        re = ur.post(data,token=self.access_token)
        msg = "FAILED {0} assert failed !!".format(sys._getframe().f_code.co_name)
        self.assertEqual(re.json()['resultCode'],'00000000',msg)
        print(re.json())


    def test_app_QueryUserInfo_1(self):
        '''查询流量包优先开关标识'''
        data = {
            "streamNo": "UKAPP20151113161019000001",
            "partnerCode": "UKAPP",
            "loginCustomerId": self.userId,
            "needPkgFirstFlag": "true"
        }
        ur = uklReq('app_QueryUserInfo')
        re = ur.post(data,token=self.access_token)
        msg = "FAILED {0} assert failed !!".format(sys._getframe().f_code.co_name)
        self.assertEqual(re.json()['data']['pkgFirstFlag'],True,msg)
        print(re.json())

if __name__ =="__main__":
    #unittest.main()
    report_path = REPORT_PATH +'\\'+get_ftime()+'_report.html'
    test_suite = unittest.TestSuite()
    test_suite.addTest(app_QueryUserInfo('test_app_QueryUserInfo_0'))
    test_suite.addTest(app_QueryUserInfo('test_app_QueryUserInfo_1'))
    with open(report_path,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='saas 接口自动化测试',description='测试报告')
        runner.run(test_suite)
