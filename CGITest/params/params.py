#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    1. ���ʱ��ע���Ű��ʽ
    2. ����ע��ĳ�� CGI �� ֻע��ĳ�� CGI �µ�ĳһ������ע��ʱֻ����ԭ�е�����ǰ�Ӹ� ��#�� �ַ�
'''

params = {
            # ��һ�� CGI �����ֺͶ�������Բ���
            'GetPresentBetInfo.cgi':[
                                         'activity_id=1'
                                         ,'activity_id=2'
                                         ,'activity_id=2'
                                    ],
            # �ڶ��� CGI �����ֺͶ�������Բ���
            'GetUserInfo.cgi':[
                                    'user_id=1'
                                    ,'user_id=2'
                              ],
            # ������ CGI ��ע�ͣ�CGI ����ǰ���и� #���������ᱻ����;���⣬Ҳ����ע������ĳ�������Բ���
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
