#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from time import time
from CRM_API_TEST.public.readConf import config,CONFIG_FILE

class loginReq(object):
    def __init__(self,tmlUserNum):
        cf = config(CONFIG_FILE)
        self.host = cf.get('host','host1')
        self.url = cf.get('apiUrl','app_QuickUserLogin')
        self.headers = {'Content-Type': 'application/json'}
        streamNo = 'AutoApiTest' + str(int(time()))
        tmlUser = cf.get(tmlUserNum,'tmlUser')
        tmlPwd = cf.get(tmlUserNum,'tmlPwd')
        enterprisecode = cf.get(tmlUserNum,'enterprisecode')
        self.data = {

                "streamNo": streamNo,
                "clientId": "id123456",
                "clientSecret": "id123456",
                "userCode": tmlUser,
                "loginType": "PWD",
                "enterpriseCode": enterprisecode,
                "password": tmlPwd,
                "channelType": "APP"
        }

    def getToken(self):
        r = requests.post(self.host+self.url,headers=self.headers,json=self.data)
        return r.json()['accessToken']
    def getUserId(self):
        r = requests.post(self.host + self.url, headers=self.headers, json=self.data)
        return r.json()['userId']
    def get(self):
        a = []
        r = requests.post(self.host + self.url, headers=self.headers, json=self.data)
        a.append(r.json()['userId'])
        a.append(r.json()['accessToken'])
        return a

class uklReq():
    def __init__(self,apiName):
        #读取配置的url
        cf = config(CONFIG_FILE)
        self.host = cf.get('host','host1')
        self.url = cf.get('apiUrl',apiName)
        self.headers = {'Content-Type':'application/json'}

    def post(self,data,token=None):
        if token == None:
            r = requests.post(self.host + self.url, json=data, headers=self.headers)
            return r
        else:
            token = '?access_token='+token
            r = requests.post(self.host + self.url + token, json=data, headers=self.headers)
            return r


