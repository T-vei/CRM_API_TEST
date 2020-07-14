#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest,requests
from CRM_API_TEST.case.interface.uklRequest import loginReq,uklReq
from CRM_API_TEST.public.readConf import config,CONFIG_FILE
from CRM_API_TEST.public.log import LOG
from CRM_API_TEST.public.HTMLTestRunner_PY3 import HTMLTestRunner
from ddt import ddt,data,file_data,unpack

class app_RegisterUser(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_app_RegisterUser(self):
        data = {
            "streamNo": "UKAPP20151113161019000001",
            "partnerCode": "UKAPP",
            "langType": "zh-CN",
            "enterpriseCode": "EA00010066",
            "registerType": "EMAIL",
            "userCode": "20200709001@cn.com",
            "password": "e10adc3949ba59abbe56e057f20f883e",
            "channelType": "APP",
            "registerCountry": "CN"
        }
        uklReqest = uklReq('app_RegisterUser')
        re = uklReqest.post(data)
        print(re.json())
        if re.status_code == 200:
            LOG.logger.info(__class__.__name__ + '  ' +  __name__ + "  request success!")
        else:
            print("request failed !!")
        assert re.json()['resultCode'] == '00000000'