#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from CRM_API_TEST.public.readConf import config,DATA_PATH

class login(object):
    def __init__(self):
        url_data = DATA_PATH + "\\api_url.conf"
        cf = config(url_data)
        host = cf.get('host','host1')
        url = cf.get()
        data = {

        }

    def loginRsp(self,username,userpwd,enterprisecode):
        r = requests.post(host+url,headers=headers,json=data)


###写一个登录用户获取token、userId的公共方法
###将接口url分离处理放在配置文件里读取，找不到就报错
###使用ddt数据驱动测试
###将接口请求的公共方法分离出来，包括去读取配置文件

