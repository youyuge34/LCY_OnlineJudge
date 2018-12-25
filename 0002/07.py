#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-25 11:06
# @Author  : YouSheng-MF1832226

'''
非递归快排
Description

快速排序的核心思想是使用元素的值对数组进行划分。实现其非递归方案。


Input

输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。


Output

输出的每一行为排序结果，用空格隔开，末尾不要空格。


Sample Input 1 

13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1

3 3 9 12 24 29 34 49 51 56 78 84 100
'''

def QuickSort(arr):
	stack = []  # 用stack来存储low，high索引代替递归
	stack.append(0)
	stack.append(len(arr)-1)

	while stack:
		high = stack.pop()
		low = stack.pop()
		# print('low,high = ',low,high)
		if low >= high:
			continue

		mid = low
		temp = arr[high]
		for i in range(low, high):	# 只有比temp小的，就把它交换到前面去，第几个不用管。
			if arr[i] <= temp:
				arr[mid], arr[i] = arr[i], arr[mid]
				mid += 1
		arr[mid], arr[high] = arr[high], arr[mid]  # mid就是中间结点
		# print(arr)
		# print('mid: ',mid)
		stack.extend([low, mid-1, mid+1, high])
	return arr



# 本地测试代码
# arr = '13 24 3 56 34 3 78 12 29 49 84 51 9 100'
# arr = list(map(int,arr.strip().split()))
# res = QuickSort(arr[1:])
# cc = ''
# for i in res:
# 	cc += str(i) + ' '
# print(cc.strip())

while 1:
	try:
		arr = list(map(int,input().strip().split()))
		res = QuickSort(arr[1:])
		cc = ''
		for i in res:
			cc += str(i) + ' '
		print(cc.strip())
	except Exception as e:
		break
