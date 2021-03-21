#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gift import have_git
import gift


# 发礼物的方法
def send():
    print("发礼物啦")
    gift.have_git = True
