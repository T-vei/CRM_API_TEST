#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import redis
from CRM_API_TEST.public.readConf import config,CONFIG_FILE

class redisdb():
    def __init__(self):
        self.redis_host = config(CONFIG_FILE).get('redis', 'redis_host').split(',', 2)
        self.redis_port = int(config(CONFIG_FILE).get('redis', 'redis_port'))
        #
    def redisConnect(self,Name):
        '''对redis集群进行遍历查询，找出有此Name的那个'''
        for host in self.redis_host:
            rds = redis.StrictRedis(host=host, port=6379, decode_responses=True)
            print('connect redis success')
            #print(host + rds.exists(Name))
            #rds.exists(Name)查不到的时候会抛异常
            try:
                if rds.exists(Name) == 0 or rds.exists(Name) == 1:
                    break
            except:
                continue
            else:
                print(Name + '  is not exist!!')
        return rds

    def hget(self,Name,rkeys):
        '''get hash key'''
        rds = self.redisConnect(Name)
        print(type(rds))
        rvalue = ''
        if rds.hexists(Name,rkeys)== True:
            rvalue = rds.hget(Name,rkeys)
        else:
            print(rkeys + 'is not found !')
        return rvalue

#rds = redisdb()
#print(rds.hkeys('RANDOM_CODE'))
#print(rds.hget('RANDOM_CODE','7872e55bc4fe4aa38d8861ba2b081ccd'))
#print(rds.hget('OSS_KEY_ALARMCONFIG','ASS_loginFailAlarm_03040001'))
#print(rds.exists('RANDOM_CODE'))
#print(rds.hexists('RANDOM_CODE','723d85fd61b34a33816a622c53c82bf5'))



