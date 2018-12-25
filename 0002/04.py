#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-25 11:06
# @Author  : YouSheng-MF1832226

'''
插入排序
Description

实现插入排序。


Input

输入的每一行代表一个数组，其中的值用空格隔开，第一个值表示数组的长度。


Output

输出排序的数组，用空格隔开，末尾不要空格。


Sample Input 1 

13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1

3 3 9 12 24 29 34 49 51 56 78 84 100
'''

def InsertSort(array):

	# while 循环写法(推荐)
	for i in range(1, len(array)):
		temp = array[i]     # 当前需要排序的元素
		index = i           # 用来记录排序元素需要插入的位置
		while index > 0 and array[index - 1] > temp:
			array[index] = array[index - 1]     # 把已经排序好的元素后移一位，留下需要插入的位置
			index -= 1
		array[index] = temp # 把需要排序的元素，插入到指定位置
	return array

	# for 循环写法
	# for i in range(1,len(array)):
	# 	temp = array[i]
	# 	j = i
	# 	for j in range(i,-1,-1):
	# 		if j == 0:
	# 			break
	# 		if array[j-1] > temp:
	# 			array[j] = array[j-1]
	# 		else: break
	# 	array[j] = temp
	# return array


# 本地测试代码
# arr = '12 56 34 3 3 78 12 29 49 84 51 9 100'
# arr = list(map(int,arr.strip().split()))
# res = InsertSort(arr[1:])
# cc = ''
# for i in res:
# 	cc += str(i) + ' '
# print(cc.strip())

while 1:
	try:
		arr = list(map(int,input().strip().split()))
		res = InsertSort(arr[1:])
		cc = ''
		for i in res:
			cc += str(i) + ' '
		print(cc.strip())
	except Exception as e:
		break
