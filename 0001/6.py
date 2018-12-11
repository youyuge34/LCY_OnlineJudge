#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-11 11:06
# @Author  : YouSheng-MF1832226

s = list(map(int,input().strip().split()))
num = int(input().strip())

s = [x for x in s if x <= num]

res = 0

while len(s)>0:
  x = s[0]
  s.pop(0)
  res += s.count(num-x)
print(res)