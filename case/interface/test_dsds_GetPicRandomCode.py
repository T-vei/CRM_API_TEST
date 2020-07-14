#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest,requests,redis
from CRM_API_TEST.case.interface.uklRequest import loginReq,uklReq
from CRM_API_TEST.public.readConf import config,CONFIG_FILE
from CRM_API_TEST.public.log import LOG
from CRM_API_TEST.public.HTMLTestRunner_PY3 import HTMLTestRunner
from ddt import ddt,data,file_data,unpack


class dsds_GetPicRandomCode(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_dsds_GetPicRandomCode(self):
        data = {
            "streamNo": "DSDS20151113161019000001",
            "partnerCode": "UKAPP",
            "langType": "zh-CN"
        }
        uklReqest = uklReq('dsds_GetPicRandomCode')
        re = uklReqest.post(data)
        print(re.json())
        if re.status_code == 200:
            LOG.logger.info(__class__.__name__ + '  ' +  __name__ + "  request success!")
        else:
            print("request failed !!")
        assert re.json()['resultCode'] == '00000000'