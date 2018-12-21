# 有一个由N个实数构成的数组，如果一对元素A[i]和A[j]是倒序的，即i<j但是A[i]>A[j]则称它们是一个倒置，设计一个计算该数组中所有倒置数量的算法。要求算法复杂度为O(nlogn)
num = int(input().strip())

def handle(length, arr):
  res = 0
  for i in range(length-1):
    for j in range(i+1,length):
      if arr[i] > arr[j]:
        res += 1
  print(res)

for x in range(num):
  length = int(input())
  arr = list(map(int,input().strip().split()))
  handle(length, arr)