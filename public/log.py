#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,threading
from datetime import datetime
import logging
import logging.config
from CRM_API_TEST.public.readConf import LOG_PATH

class mylog(object):
    def __init__(self):
        #create log dir
        if not os.path.exists(LOG_PATH):
            os.mkdir(LogPath)
        logPath = os.path.join(LOG_PATH,str(datetime.now().strftime("%Y-%m-%d")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        #read logging config file
        #logging.config.fileConfig("../conf/logging.conf")

        #create logger
        logger_name = "testlog"
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        #create file handler
        log_path = '../log/log.log'
        fh = logging.FileHandler(os.path.join(logPath,(str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + "-log.log")))
        fh.setLevel(logging.DEBUG)

        #create formatter
        fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
        datefmt = "%a %d %b %Y %H:%M:%S"
        formatter = logging.Formatter(fmt, datefmt)

        #add handler and formatter to logger
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
'''
#print logging info
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
'''
#单独的线程处理日志任务

class logger(object):
    log = None
    mutex = threading.Lock()
    @staticmethod
    def logit():
        if logger.log is None:
            logger.mutex.acquire()
            logger.log = mylog()
            logger.mutex.release()

        return logger.log

LOG = logger.logit()
'''
if __name__=='__main__':
    LOG.logger.debug('test log debug !!!!')
    LOG.logger.info('test log info !!!!')
    LOG.logger.warning('test log warn !!!!')
    LOG.logger.error('test log error !!!!')
    
'''