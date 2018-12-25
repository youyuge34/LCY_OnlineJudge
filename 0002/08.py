#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-25 11:06
# @Author  : YouSheng-MF1832226

'''
非递归合并排序
Description

合并（归并）排序的核心思想是：每次从中间位置将数组分组再分别排序。请实现其非递归方案。


Input

输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。


Output

输出的每一行为排序结果，用空格隔开，末尾不要空格。


Sample Input 1 

13 24 3 56 34 3 78 12 29 49 84 51 9 100
Sample Output 1

3 3 9 12 24 29 34 49 51 56 78 84 100
'''


# https://www.jianshu.com/p/3f27384387c1
def merge(low, mid, high, arr):
	s = arr[low:mid].copy()
	m = arr[mid:high].copy()
	res = []
	while s and m:
		if s[0] <= m[0]:
			res.append(s.pop(0))
		else : res.append(m.pop(0))
	res.extend(s)
	res.extend(m)
	arr[low:high] = res
	


def MergeSort(arr):
	i = 1 #子数组长度, 合并最后整个数组是一个子数组
	while i < len(arr):

		# 求出每2个子数组的（low，mid，high），合并 [low,mid) [mid,high)
		low = 0
		while low < len(arr):
			mid = low + i
			high = min(mid + i, len(arr))
			if mid < high:
				merge(low, mid, high, arr)

			low = high
		i *= 2
	return arr





# 本地测试代码
# arr = '12 56 34 3 3 78 12 29 49 84 51 9 100'
# arr = list(map(int,arr.strip().split()))
# res = MergeSort(arr[1:])
# cc = ''
# for i in res:
# 	cc += str(i) + ' '
# print(cc.strip())

while 1:
	try:
		arr = list(map(int,input().strip().split()))
		res = MergeSort(arr[1:])
		cc = ''
		for i in res:
			cc += str(i) + ' '
		print(cc.strip())
	except Exception as e:
		break
