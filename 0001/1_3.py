#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-11 11:06
# @Author  : YouSheng-MF1832226

def getNnum(arr,num):
  res = 0
  length = len(arr)
  for i in range(length):
    temp = 0 #
    for j in range(i+1,length):
      if abs(arr[i]-arr[j])>num:
        # 符合题意的min，max找到了~
        res += pow(2,length-i-2-temp)
        temp += 1
  return res


arr = list(map(int,input().strip().split()))
num = int(input().strip())
res = getNnum(arr, num)
print(res)