#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from configparser import ConfigParser

#项目的文件目录地址，支持不同操作系统
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'conf', 'config.conf')
DATA_PATH = os.path.join(BASE_PATH, 'data')
API_DATA_PATH = os.path.join(BASE_PATH, 'data','api_url.conf')
PUBLIC_PATH = os.path.join(BASE_PATH, 'public')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
current_dir = os.path.abspath(os.path.join(os.getcwd(),'..','config','config.conf'))  #当前文件所在目录的父目录的conf目录
config_dir = '../conf/config.conf'
report = REPORT_PATH +'\\report.html'

'''
#目录测试
print(BASE_PATH)
print(CONFIG_FILE)
print(DATA_PATH)
print(PUBLIC_PATH)
print(LOG_PATH)
print(REPORT_PATH)
print(os.getcwd())
'''
#读取conf配置
class config():
    def __init__(self,config_file):
        self.conf = ConfigParser()
        self.conf.read(config_file, encoding="UTF-8")

    def get(self,section,option):
        return self.conf.get(section,option)
    def sections(self):
        return self.conf.sections()

'''
if __name__== '__main__':
    s =config(CONFIG_FILE)
    print(s.get('section1','host1'))
    print(s.sections())

'''
