#!/usr/bin/python
# -*- coding: UTF-8 -*-

from constants import DEST_PATH
from constants import SOURCE_PATH
from constants import URL
import os

def checkPath(path):
    if os.path.exists(path) == False:
        raise Exception("path is not exists", path)
    if path[len(path)-1:len(path)] != os.sep:
        path = path + os.sep
    return path

def checkUrl(url):
    if url[len(url)-1:len(url)] != '/':
        url = url + '/'
    return url

DEST_PATH = checkPath(DEST_PATH)
SOURCE_PATH = checkPath(SOURCE_PATH)
URL = checkUrl(URL)
