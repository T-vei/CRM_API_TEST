#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest,requests
from CRM_API_TEST.case.interface.uklRequest import loginReq,uklReq
from CRM_API_TEST.public.readConf import config,CONFIG_FILE,REPORT_PATH
from CRM_API_TEST.public.log import LOG
from CRM_API_TEST.public.HTMLTestRunner_PY3 import HTMLTestRunner
from ddt import ddt,data,file_data,unpack

class app_QueryUserOfferList(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_app_QueryUserOfferList(self):
        lg = loginReq('tmlUser1')
        access_token = lg.get()[1]
        userId = lg.get()[0]
        print(userId)
        print(access_token)
        data = {
            "streamNo": "GLCAM20151113161019000001",
            "partnerCode": "UKAPP",
            "loginCustomerId": userId,
            "langType": "zh-CN",
            "goodsType": "PKAG",
            "currentPage ": 1,
            "perPageCount": 10,
            "flag": 0,
            "iso2": "CN",
            "customerId": userId
        }
        uklReqest = uklReq('app_QueryUserOfferList')
        re = uklReqest.post(data,token=access_token)
        print(re.json())
        if re.status_code == 200:
            LOG.logger.info(__class__.__name__ + '  ' +  __name__ + "  request success!")
        else:
            print("request failed !!")
        assert re.json()['resultCode'] == '00000000'


if __name__ =="__main__":
    #unittest.main()
    report = REPORT_PATH +'\\report.html'
    print(report)
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='saas 接口自动化测试',description='测试报告')
        runner.run(app_QueryUserOfferList('test_app_QueryUserOfferList'))