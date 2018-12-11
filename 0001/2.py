#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-11 11:06
# @Author  : YouSheng-MF1832226

def maxRec(height):
  # 计算直方图中的最大矩形面积
  res = 0
  length = len(list(height))
  for i in range(length):
    if i+1<length and height[i]<height[i+1]:
      continue
    minH = height[i]

    for j in range(i,-1,-1):
      minH = min(minH, height[j])
      area = minH * (i-j+1)
      res = max(res, area)
  return res


# data = [[1,0,1,1],[1,1,1,1],[1,1,1,0],[1,1,1,1]]
data = []
while 1:
  try:
  	data.append(list(map(int, input().strip().split())))
  except Exception as e:
  	break

res = 0
row = len(data)
col = len(data[0])
height = [0]*col

for i in range(row):
  for j in range(col):
  	if data[i][j] == 0:
  	  height[j] = 0
  	else:
  	  height[j] += 1
  res = max(res, maxRec(height))
print(res)