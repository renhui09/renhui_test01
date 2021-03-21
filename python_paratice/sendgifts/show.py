#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from gift import have_git
import gift


# 展示礼物
def show():
    have_git = gift.have_git
    if have_git == True:
        print("收到礼物啦，好开心～")
    else:
        print("没有礼物")
