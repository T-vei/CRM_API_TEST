#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests


url = 'http://10.1.77.182:9092/bss/grp/user/CheckSubUserPassword?access_token=TGT-128238-DtfY2JKIpGclVqrURAnMnhanUeeghDBSGdswKWM2IDWYPOZaCB'
data = {
    "loginCustomerId": "59ca12664d9b231c516342b2",
    "partnerCode": "UKSAS",
    "streamNo": "web_saas20200721000001",
    "password": "e10adc3949ba59abbe56e057f20f883e1",
    "userCode": "301000017918"
}
headers = {'Content-Type':'application/json'}


re = requests.post(url,json=data,headers=headers)

print(re.json())