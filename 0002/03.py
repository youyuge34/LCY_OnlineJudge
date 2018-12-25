#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-24 11:06
# @Author  : YouSheng-MF1832226

'''
链表区间逆序
Description

将单个链表的每K个节点之间逆序，打印出新链表；最后不足K的节点数不需要逆序；要求时间复杂度为O(n)，额外空间复杂度为O(1)。


Input

输入的每一行的值用空格隔开，第一个表示链表长度，中间为节点值，最后代表K。


Output

输出的每一行为新的链表，节点值用空格隔开，末尾不要空格。

Sample Input 1 

8 1 2 3 4 5 6 7 8 3
8 a b c d e f g h 4
Sample Output 1

3 2 1 6 5 4 7 8
d c b a h g f e

'''

class Node(object):
	"""docstring for Node"""
	def __init__(self, arg):
		super(Node, self).__init__()
		self.data = arg
		self.next = None

class LinkList(object):
	def __init__(self, data):
		assert data[0] is not None
		self.head = Node(data[0])

		p = self.head
		for i in data[1:]:
			p.next = Node(i)
			p = p.next

def reverse(arr, k, length):
	'''
	第二题的链表逆序懂的话这里就非常容易了，current节点逆序完会到下一个区间的第一个节点，
	小区间的末尾prev结点正好变头节点，直接继续遍历即可。
	这里为了简单并未将所有区间链接起来，而是每次小区间逆序完就输出
	'''
	if k>length:
		k = length
	if k <= 0:
		k = 1
	nparts = length // k
	# print('nparts:',nparts)
	current = arr.head
	res = ''
	for i in range(nparts):
		prev = None
		for x in range(k):
			temp = current.next # 记录下下一个，因为我们要断开链表了
			current.next = prev # 下一个变为前面一个Node，实现反转。第一次指向None，代表末尾节点
			# prev 和 current节点都要向前移位一个啦
			prev = current
			current = temp
		# print(prev)
		hh = prev
		for x in range(k):
			res += str(hh.data) + ' '
			hh = hh.next
		# print(prev)
		# print(res)
	while current:
		res += str(current.data) + ' '
		current = current.next
	return res.strip()

# 本地测试代码
# data = [[8,1,2,3,4,5,6,7,8,3],[8,'a','b','c','d','e','f','g','h',4],[6,1,2,3,4,5,6,2], \
# 			[8,1,2,3,4,5,6,7,8,4],[8,1,2,3,4,5,6,7,8,101],[8,1,2,3,4,5,6,7,8,8],[8,1,2,3,4,5,6,7,8,1]]
# for ll in data:
# 	res = reverse(LinkList(ll[1:-1]), int(ll[-1]), len(ll)-2)
# 	print(res.strip())

while 1:
	try:
		arr = list(input().strip().split())
		res = reverse(LinkList(arr[1:-1]), int(arr[-1]), len(arr)-2)
		print(res.strip())
	except Exception as e:
		break
