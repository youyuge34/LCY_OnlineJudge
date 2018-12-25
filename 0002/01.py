#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-24 11:06
# @Author  : YouSheng-MF1832226

'''
最长公共子序列
Description

给定两个字符串，返回两个字符串的最长公共子序列（不是最长公共子字符串），可能是多个。


Input

输入为两行，一行一个字符串


Output

输出如果有多个则分为多行，先后顺序不影响判断。


Sample Input 1 

1A2BD3G4H56JK
23EFG4I5J6K7
Sample Output 1

23G456K
23G45JK
'''
def LCS(x, y):
	# 返回dp table 和 最大长度
	len_x = len(x)
	len_y = len(y)
	# 必须这样创建，避免py的浅拷贝
	dp = [[0 for i in range(len_y+1)] for i in range(len_x+1)]

	for i in range(len_x):
		for j in range(len_y):
			# 注意此处子串的位置i对应dp table里的i+1位置
			if x[i] == y[j]:
				dp[i+1][j+1] = int(dp[i][j]) + 1
			else:
				dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

	return dp, dp[len_x][len_y]

 


def res(dp, length, i, j, x, y, ans, aa):
	
	# aa = set()
	while i>0 and j>0:
		if x[i-1] == y[j-1]:
			ans += str(x[i-1])
			# print(ans)
			i -= 1
			j -= 1
		else:
			if dp[i-1][j] > dp[i][j-1]:
				i -= 1  # 上面的大，回溯往上走
			elif dp[i-1][j] < dp[i][j-1]:
				j -= 1
			else:
				# 递归
				res(dp, length, i-1, j, x, y, ans, aa)
				res(dp, length, i, j-1, x, y, ans, aa)
				return
	# print(ans)
	if len(ans.strip())==length:	
		aa.add(ans.strip()[::-1])
	# 	print(ans)
	# print(aa)
	# return aa

arr1 = str(input().strip())
arr2 = str(input().strip())
dp, length = LCS(arr1, arr2)
aa = set()
res(dp, length, len(arr1), len(arr2), arr1, arr2, "", aa)
for res in aa:
	print(res)

