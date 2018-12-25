#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-25 11:06
# @Author  : YouSheng-MF1832226

'''
冒泡排序
Description

实现冒泡排序。


Input

输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。


Output

输出的每一行为排序结果，用空格隔开，末尾不要空格。


Sample Input 1 

13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1

3 3 9 12 24 29 34 49 51 56 78 84 100
'''

def BubbleSort(arr):
	for i in range(len(arr)):
		for j in range(1,len(arr)-i):
			if arr[j-1] > arr[j]:
				arr[j-1], arr[j] = arr[j], arr[j-1]
	return arr


# 本地测试代码
# arr = '13 24 3 56 34 3 78 12 29 49 84 51 9 100'
# arr = list(map(int,arr.strip().split()))
# res = BubbleSort(arr[1:])
# cc = ''
# for i in res:
# 	cc += str(i) + ' '
# print(cc.strip())

while 1:
	try:
		arr = list(map(int,input().strip().split()))
		res = BubbleSort(arr[1:])
		cc = ''
		for i in res:
			cc += str(i) + ' '
		print(cc.strip())
	except Exception as e:
		break
