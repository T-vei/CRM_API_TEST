#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import unittest,requests
from CRM_API_TEST.public.readConf import config
from CRM_API_TEST.public.readConf import LOG_PATH,REPORT_PATH
from CRM_API_TEST.public.log import LOG
from CRM_API_TEST.public.HTMLTestRunner_PY3 import HTMLTestRunner
from ddt import ddt,data,data_file,unpack

class QueryOfferList(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_QueryOfferList(self):
        data = {
            "bgTime": 0,
            "channelType": "APP",
            "currentPage": 1,
            "diyFlag": 0,
            "endTime": 0,
            "langType": "zh-CN",
            "loginCustomerId": "5eb92e20e5cab40c2c82af13",
            "mcc": "CN",
            "mccFlag": "WHITE",
            "mvnoCode": "GCGROUP",
            "partnerCode": "GCGROUP",
            "perPageCount": 200,
            "queryPromotionFlag": true,
            "streamNo": "APP20200512013450895110",
            "terminalType": "APP"
        }
        r = requests.post()