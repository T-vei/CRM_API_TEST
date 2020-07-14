#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest,requests
from CRM_API_TEST.case.interface.uklRequest import loginReq,uklReq
from CRM_API_TEST.public.readConf import config,CONFIG_FILE
from CRM_API_TEST.public.log import LOG
from CRM_API_TEST.public.HTMLTestRunner_PY3 import HTMLTestRunner
from ddt import ddt,data,file_data,unpack


class app_QueryUserInfo(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_app_QueryUserInfo_0(self):
        lg = loginReq('tmlUser1')
        access_token = lg.get()[1]
        userId = lg.get()[0]
        data = {
            "streamNo": "UKAPP20151113161019000001",
            "partnerCode": "UKAPP",
            "loginCustomerId": userId
        }
        ur = uklReq('app_QueryUserInfo')
        re = ur.post(data,token=access_token)
        print(userId)
        print(access_token)
        print(re.status_code)
        print(re.content)
        print(re.json())


if __name__ =="__main__":
    unittest.main()
