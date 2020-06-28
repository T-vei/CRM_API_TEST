#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import unittest,requests
from CRM_API_TEST.public.readConf import config
from CRM_API_TEST.public.readConf import LOG_PATH,REPORT_PATH
from CRM_API_TEST.public.log import LOG
from CRM_API_TEST.public.HTMLTestRunner_PY3 import HTMLTestRunner

class app_QuickUserLogin(unittest.TestCase):
    def setUp(self):
        cf = config()
        #global host,tmlUser,tmlPwd
        self.host = cf.get("section1","host1")
        self.tmlUser = cf.get("section3","tmlUser")
        self.tmlPwd = cf.get("section3","tmlPwd")
        #print(self.host,self.tmlUser)


    def test_appQuickUserLogin(self):
        url = "/bss/app/noauth/QuickUserLogin"
        #print(host + url)
        headers = {'Content-Type':'application/json'}
        data = {

                "streamNo": "GLCAM20206273161019000001",
                "clientId": "id123456",
                "clientSecret": "id123456",
                "userCode": self.tmlUser,
                "loginType": "PWD",
                "enterpriseCode": "EA00010066",
                "password": self.tmlPwd,
                "channelType": "APP"

        }
        r = requests.post(self.host + url,headers=headers,json=data)
        print(r.status_code)
        print(r.json()['resultCode'])
        self.assertEqual(r.json()['resultCode'],'00000000')
        LOG.logger.info(self.__class__.__name__)
        LOG.logger.info(r.content)

    def tearDown(self):
        pass

if __name__ =="__main__":
    #unittest.main()
    report = REPORT_PATH +'\\report.html'
    print(report)
    with open('../report/report.html','wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='saas 接口自动化测试',description='测试报告')
        runner.run(app_QuickUserLogin('test_appQuickUserLogin'))

