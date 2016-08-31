#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    DEST_PATH：CGI 需要拷贝到的完整目录
    SOURCE_PATH：待测试的 CGI 的存放父目录，可以设置为项目的根目录，程序可以递归查找
    URL：请求的 url 地址，这个地址会与 CGI 名字拼接，成为一个完整的 CGI url 地址；注意：不要带 "http(s):://"
'''

DEST_PATH = r'your_path_copyto'
SOURCE_PATH = r'your_path_copyfrom'
URL = r'www.python.org'
