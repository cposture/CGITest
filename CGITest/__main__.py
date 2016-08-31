#!/usr/bin/python
# -*- coding: UTF-8 -*-

from install import *
from params import *
from excute import *
from textstyle import *

def main():
    count = 0
    for cginame in params:
        if isCommentParam(cginame):
            continue
        for param in params[cginame]:
            if isCommentParam(param):
                continue
            print UseStyle("[" + str(count) + "]", back = 'blue') + UseStyle(cginame + "\t" + param, fore = 'green')
            # �������Ե� CGI ��ָ��Ŀ¼
            installCGI(cginame)
            # ִ�и� CGI
            print UseStyle("response result :", fore = 'green')
            print "\t" + excuteCGI(URL + cginame, param)
            count = count + 1

if __name__ == "__main__":
    main()
