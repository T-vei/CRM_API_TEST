#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest,requests,os
from CRM_API_TEST.public.readConf import config
from CRM_API_TEST.public.readConf import LOG_PATH,REPORT_PATH,CONFIG_FILE
from CRM_API_TEST.public.log import LOG
from CRM_API_TEST.public.HTMLTestRunner_PY3 import HTMLTestRunner
from ddt import ddt,data,file_data,unpack

@ddt
class aaa(unittest.TestCase):
    s = '9'
    def setUp(self):
        self.a = '1'
    def tearDown(self):
        pass
    @data({'b':'1','c':'2','d':self.a})
    def test_aasasa(self,data):
        print(data)


print(os.path.abspath(__file__))


'''
if __name__ =="__main__":
    unittest.main()

'''