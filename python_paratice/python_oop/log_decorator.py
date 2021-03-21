#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

# 设置基本日志
logging.basicConfig(level=logging.DEBUG)

# 自定义logger
logger = logging.getLogger('log')


# 定义装饰器(func表示函数)
# *args,**kwargs表示万能函数的接收
def log_decorator(func):
    '''
    给传入的函数添加日志信息
    :param func:传入的函数
    :return:添加了log信息的函数
    '''

    def wrapper(*args, **kwargs):
        # 加上log信息
        logger.debug(f"装饰器：{log_decorator.__name__} -> 传入函数：{func.__name__}")
        # 调用传入的函数对象
        return func(*args, **kwargs)

    return wrapper
