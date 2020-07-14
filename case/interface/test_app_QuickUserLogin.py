#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest,requests
from CRM_API_TEST.public.readConf import config
from CRM_API_TEST.public.readConf import LOG_PATH,REPORT_PATH,CONFIG_FILE
from CRM_API_TEST.public.log import LOG
from CRM_API_TEST.public.HTMLTestRunner_PY3 import HTMLTestRunner
from ddt import ddt,data,file_data,unpack

@ddt
class app_QuickUserLogin(unittest.TestCase):
    cf = config(CONFIG_FILE)
    # global host,tmlUser,tmlPwd
    host = cf.get("host", "host1")
    tmlUser = cf.get("tmlUser", "tmlUser1")
    tmlPwd = cf.get("tmlUser", "tmlPwd1")
    def setUp(self):
        pass
        #print(self.host,self.tmlUser)

    @data(
        ({

                "streamNo": "GLCAM20206273161019000001",
                "clientId": "id123456",
                "clientSecret": "id123456",
                "userCode": tmlUser,
                "loginType": "PWD",
                "enterpriseCode": "EA00010066",
                "password": tmlPwd,
                "channelType": "APP"

        },"00000000"),
            ({

            "streamNo": "GLCAM20206273161019000001",
            "clientId": "id123456",
            "clientSecret": "id123456",
            "userCode": "",
            "loginType": "PWD",
            "enterpriseCode": "EA00010066",
            "password": tmlPwd,
            "channelType": "APP"

        }, "01020004")
    )
    @unpack
    def test_appQuickUserLogin(self,data,code):
        url = "/bss/app/noauth/QuickUserLogin"
        #print(host + url)
        headers = {'Content-Type':'application/json'}
        r = requests.post(self.host + url,headers=headers,json=data)
        self.assertEqual(r.json()['resultCode'], code)
        print(r.status_code)
        print(r.json()['resultCode'])
        print(r.json()['resultDesc'])
        print(r.content)
        LOG.logger.info(self.__class__.__name__)
        LOG.logger.info(r.content)

    def tearDown(self):
        pass

if __name__ =="__main__":
    #unittest.main()
    report = REPORT_PATH +'\\report.html'
    print(report)
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='saas 接口自动化测试',description='测试报告')
        runner.run(app_QuickUserLogin('test_appQuickUserLogin'))

