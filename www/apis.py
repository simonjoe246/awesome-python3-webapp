#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Simon    time:2018/3/10


'''
JSON API defination
'''


import json, logging, inspect, functools

class APIError(Exception):
    '''
    the base APIError which contains error(required), data(optional) and message(optional)
    '''
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    '''
    Indicate the input value has error or invalid. The data specifies the error field and input form.
    '''
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value: invalid', field, message)


class APIResourceNotFound(APIError):
    '''
    Indicate the resource was not found. The data specifies the resource name
    '''
    def __init__(self, field, message=''):
        super(APIResourceNotFound, self).__init__('value: not found', field, message)


class APIPermissionError(APIError):
    '''
    Indicate the api has no permission
    '''
    def __init__(self, message):
        super(APIPermissionError, self).__init__('permission: forbidden', 'permission', message)
