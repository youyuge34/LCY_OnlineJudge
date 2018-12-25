#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-12-24 11:06
# @Author  : YouSheng-MF1832226

'''
链表回文
Description

判断一个单向链表是否为回文结构。自定义链表数据结构，要求时间复杂度为O(n)，额外空间复杂度为O(1)。


Input

输入的每一行的值用空格隔开，第一个值为节点个数，后面为每一个节点值


Output

是回文则输出true，不是则输出false，一行表示一个链表的结果。


Sample Input 1 

3 1 2 1
4 1 2 2 1
3 3 5 3
6 a b c d c a
Sample Output 1

true
true
true
false
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

# https://www.cnblogs.com/lightwindy/p/8628183.html
# https://blog.csdn.net/zhenghaitian/article/details/81025147
def isHuiWen(arr):
	# 1. 追赶法得到中点 current
	head = arr.head
	# print(head.data)
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	prev = None
	current = slow
	# print(head.data,current.data)
	# print(current.data)
	# 2. 复杂的后半部分链表反转
	while current:
		temp = current.next # 记录下下一个，因为我们要断开链表了
		current.next = prev # 下一个变为前面一个Node，实现反转。第一次指向None，代表末尾节点
		# prev 和 current节点都要向前移位一个啦
		prev = current
		current = temp
	 # 注意！！！最后一次的时候prev成了最后的节点（即head），current结点成了None
	# print(prev.data)
	# print(prev.next.data)

	# 3. 链表比较
	while prev and head: # now the prev is the last node!
		# start to compare
		if prev.data != head.data:
			return False
		prev = prev.next
		head = head.next
	return True

# 本地测试数据
# data = [[1,2,1],[1,2,2,1],[3,3,4,3],['a','b','c','b','a',]]
data = []
while 1:
	try:
		data.append(list(input().strip().split())[1:])
	except Exception as e:
		break
for i in range(len(data)):
	ans = isHuiWen(LinkList(data[i]), )
	if ans:
		print('true')
	else: print('false')