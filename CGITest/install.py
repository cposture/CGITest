#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
from constants import *
from textstyle import *

def backupCGI(cgipath):
    '''����������Ϊ xxx.bak'''
    current_file = cgipath
    new_file = cgipath + ".bak"

    if os.path.exists(current_file) == False:
        raise Exception("backupCGI error :the path is not found", current_file)

    print current_file
    # ������� new_file �Ѵ��ڣ����� UNIX �лᱻ���ǣ����� windows �»����쳣��
    try:
        os.rename(current_file, new_file)
    except OSError:
        os.remove(new_file)
        os.rename(current_file, new_file)

def findCGI(specific_file, search_directory):
    '''�ݹ����ָ���ļ�'''
    for i in os.walk(search_directory):
        if specific_file in i[2]:
            return i[0] + os.sep + specific_file
    raise Exception("the path is not found", specific_file)

def installCGI(cginame, isbackup = True):
    '''��װ CGI'''
    pass
    dest_cgi_path = DEST_PATH + cginame

    # Դ·���µݹ���� cginame
    source_cgi_path = findCGI(cginame, SOURCE_PATH)
    print UseStyle("\tfind ",   fore = 'yellow'),
    print source_cgi_path

    # ������Ŀ��·���� CGI
    if isbackup and os.path.exists(dest_cgi_path):
        print UseStyle("\trename ",   fore = 'yellow'),
        print dest_cgi_path[dest_cgi_path.rfind(os.sep)+1:] + " " + dest_cgi_path[dest_cgi_path.rfind(os.sep)+1:] + ".bak",
        backupCGI(dest_cgi_path)

    # ��ԴĿ¼�µ� CGI ����Ŀ��Ŀ¼
    print UseStyle("\tcopy ",   fore = 'yellow'),
    print source_cgi_path[source_cgi_path.rfind(os.sep)+1:] + " " + source_cgi_path[source_cgi_path.rfind(os.sep)+1:]
    shutil.copyfile(source_cgi_path, dest_cgi_path)
    shutil.copystat(source_cgi_path, dest_cgi_path)
