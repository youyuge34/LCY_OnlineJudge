#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-25 11:06
# @Author  : YouSheng-MF1832226

'''
计数排序
Description

实现计数排序，通过多次遍历数组，统计比每一个元素小的其它元素个数，根据该统计量对数据进行排序。


Input

输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。


Output

输出的每一行为排序结果，用空格隔开，末尾不要空格。


Sample Input 1 

13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1

3 3 9 12 24 29 34 49 51 56 78 84 100
'''

def CountSort(arr):
	ans = [0] * len(arr)
	flags = [False] * len(arr)  # 为了优化：数字遍历过的标志位，重复数字就可以skip了
	for i in range(len(arr)):
		if flags[i]:
			continue

		smaller = 0 # 存储比当前小的个数
		eq = 0 # 存储相等的个数
		for j in range(len(arr)):
			if arr[j] < arr[i]:
				smaller += 1
			if arr[j] == arr[i]:
				flags[j] = True
				eq += 1
		for x in range(smaller, smaller+eq):
			ans[x] = arr[i]
	return ans

# 本地测试代码
# arr = '13 24 3 56 34 3 78 12 29 49 84 51 9 100'
# arr = list(map(int,arr.strip().split()))
# res = CountSort(arr[1:])
# cc = ''
# for i in res:
# 	cc += str(i) + ' '
# print(cc.strip())

while 1:
	try:
		arr = list(map(int,input().strip().split()))
		res = CountSort(arr[1:])
		cc = ''
		for i in res:
			cc += str(i) + ' '
		print(cc.strip())
	except Exception as e:
		break
