#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-11 11:06
# @Author  : YouSheng-MF1832226

s = list(map(int,input().strip().split()))
a,b = list(map(int,input().strip().split()))
s = sorted(s[a-1:b])
k = int(input().strip())

print(s[k-1])

