#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-11 11:06
# @Author  : YouSheng-MF1832226

s = list(map(int,input().strip().split()))
win = int(input().strip())
length = len(s) # 8
start = 0
end = start + win # 8
out = 0
while 1:
  if end > length:
    break
  out += max(s[start:end])
  start += 1
  end += 1
print(out)