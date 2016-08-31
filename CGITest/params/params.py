#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    1. 添加时请注意排版格式
    2. 可以注释某个 CGI 或 只注释某个 CGI 下的某一参数，注释时只需在原有的名字前加个 ‘#’ 字符
'''

params = {
            # 第一个 CGI 的名字和多个待测试参数
            'GetPresentBetInfo.cgi':[
                                         'activity_id=1'
                                         ,'activity_id=2'
                                         ,'activity_id=2'
                                    ],
            # 第二个 CGI 的名字和多个待测试参数
            'GetUserInfo.cgi':[
                                    'user_id=1'
                                    ,'user_id=2'
                              ],
            # 第三个 CGI 被注释（CGI 名字前面有个 #），它不会被测试;另外，也可以注释其中某个待测试参数
            '#GetUserInfo.cgi':[
                                    '#user_id=1'
                                    ,'user_id=2'
                              ],

        }

def isCommentParam(param):
    if param and param[0] == '#':
        return True
    else:
        return False
