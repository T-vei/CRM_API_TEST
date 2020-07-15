#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

import unittest
#导入测试用例文件的类
from CRM_API_TEST.case.interface.test_app_QueryUserInfo import app_QueryUserInfo
from CRM_API_TEST.case.interface.test_dsds_GetPicRandomCode import dsds_GetPicRandomCode
'''
:方法一：单个添加测试方法到suite中
#实例化TestSuite类
suite = unittest.TestSuite()
#调用addTest方法添加测试用例类下面的测试方法
suite.addTest(app_QueryUserInfo('test_app_QueryUserInfo_0'))
suite.addTest(dsds_GetPicRandomCode('test_dsds_GetPicRandomCode'))

'''
'''
:方法二：使用makeSuite添加整个class下的测试方法到suite中

#使用makeSuite()方法直接加载一整个测试类class
suite = unittest.TestSuite(unittest.makeSuite(app_QueryUserInfo))
'''

#方法三：使用discover()方法加载整个目录下的所有用例
suite = unittest.TestLoader().discover("case")

if __name__ == '__main__':
    # 实例化runner执行器，调用run方法执行测试套件suite里的用例
    runner = unittest.TextTestRunner()
    runner.run(suite)


