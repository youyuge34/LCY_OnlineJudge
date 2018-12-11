#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-11 11:06
# @Author  : YouSheng-MF1832226

m = list(map(int,input().strip().split()))
n = list(map(int,input().strip().split()))

sum_m = sum(m)
sum_n = sum(n)

diff = sum_m - sum_n # list 总差值

while abs(diff)>0:
  best_i,best_j = 0,0 # 最好的当前交换元素的index
  best_diff = 0 # 两个交换元素的差值
  for i in range(len(m)):
    for j in range(len(n)):
      # swap 之后的新list差值diff为diff-2*(m[i]-n[j])，我们希望它的绝对值越小越好！
      # 所以先遍历搜索，找到一组交换用的i，j使得abs（新list diff）最小
      if abs(diff-2*(m[i]-n[j]))<abs(diff-2*best_diff):
        best_diff = m[i]-n[j]  #最好的一组交换元素差值
        best_i,best_j = i,j
  
  if best_diff == 0:
    break
  m[best_i],n[best_j] = n[best_j],m[best_i]
  sum_m = sum(m)
  sum_n = sum(n)

  diff = sum_m - sum_n

print(diff*2)

