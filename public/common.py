#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

def get_ftime():
    return time.strftime("%Y%m%d%H%M%S")

def get_timestamp():
    return str(time.time()*1000).split('.')[0]

