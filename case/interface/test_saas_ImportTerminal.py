#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest,requests,csv,time,random
from CRM_API_TEST.case.interface.uklRequest import loginReq,uklReq
from CRM_API_TEST.public.readConf import config,CONFIG_FILE,DATA_PATH
from CRM_API_TEST.public.log import LOG
from CRM_API_TEST.public.HTMLTestRunner_PY3 import HTMLTestRunner
from ddt import ddt,data,file_data,unpack


class saas_ImportTerminal():
    def __init__(self):
        pass
    def test_saas_ImportTerminal(self,imei):
        host = 'https://saas82.ukelink.net'
        url = '/bss/terminal/ImportTerminal'
        token = 'TGT-122815-qCTL7m9dS1PLbBWrKs0eVhwi1VYKCqYZny7cyAvliySScby0Ac'
        loginCustomerId = '5b2a3b774d9b230f50014972'
        data = {
            "streamNo": "1234567890",
            "loginCustomerId": loginCustomerId,
            "partnerCode": "UKSAS",
            "terminalList": [{
                "ownerType": "1",
                "softVersion": "1.1.1",
                "imei": imei,
                "state": "NORMAL",
                "code": imei,
                "type": "G3",
                "password": "123456",
                "orgCode": "SAPPHIREORG",
                "description": "接口自动化测试批量导入",
                "name": imei,
                "hardVersion": "1.0.0",
                "seedIccid": imei+"111"
            }]

        }
        re = requests.post(host+url+'?access_token='+token,headers = {'Content-Type':'application/json'},json=data)
        print(re.status_code)
        print(re.json())

class file_csv():
    def __init__(self,filename):
        self.path = DATA_PATH + '\\'+ filename
    def create_csv(self,csvhead):

        with open(self.path,'w',encoding='utf8',newline='') as f:
            csv_write = csv.writer(f)
            #csv_head = ['imei']
            csv_write.writerow(csvhead)

    def write_csv(self,data):
        try:
            with open(self.path,'a+',encoding='utf8',newline='') as f:
                csv_write = csv.writer(f)
                #data_row = []
                #data_row = [data]
                csv_write.writerow(data)
        except Exception:
            raise Exception

    def read_csv(self):

        data_list = ['12345678900000']
        with open(self.path,'r',encoding='utf8',newline='') as f:
            csv_read = csv.reader(f)
            for line in csv_read:
                data_list.append(line)
        return data_list

class generate_data():
    def __init__(self):
        pass
    def time(self,r='t'):
        timestamp  = str(time.time()).replace('.','')[:13]   #13位时间戳字符串-毫秒
        fdate = str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        if r == 't':
            return timestamp
        elif r == 'd':
            return fdate

    def randonNum(self,n):
        r = str(random.random()).split('.')[1]
        return r[:n]

class batchImportTerminal():
    def __init__(self):
        try:
            csv_head = ['imei']
            csv = file_csv('imei_temp.csv')
            csv.create_csv(csv_head)
            d = generate_data().time(r='d')[:11]
            for i in range(1, 5000):
                imei = ''
                imei = d + f'{i / 10000:.4f}'.split('.')[1]
                print(imei)
                print(type(imei))
                csv.write_csv(imei)
                saas_ImportTerminal().test_saas_ImportTerminal(imei)
        except:
            print("failed!!!!!!!!!!!!!!!")





if __name__ == '__main__':
    c = file_csv('redata.csv')
    c.create_csv(['imei', 'user'])
    datalist = ['123456', '202007200001@sa.com']
    c.write_csv(datalist)




