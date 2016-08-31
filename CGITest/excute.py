#!/usr/bin/python
# -*- coding: UTF-8 -*-

import httplib
from constants import *

def excuteCGI(url, params):
    host_name = url[0:url.find('/')]
    hpath = url[url.find('/'):]

    conn = httplib.HTTPSConnection(host= host_name, timeout=10)
    conn.request("POST", hpath, params)
    response = conn.getresponse()

    return response.read()
