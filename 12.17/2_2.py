import copy
num = int(input().strip())

def handle(length, arr_s):
  arr = copy.deepcopy(arr_s)
  arr_s = sorted(arr_s)
  # print(arr)
  # print(arr_s)
  index = [0] * 1001
  res = 0
  for i in range(length):
    index[arr_s[i]] = i # 记录下标索引: 每个数字应当在的位置是几
  loops = 0
  flag = [0] * length
  for i in range(length):
    if(flag[i]==0):
      j = i
      while flag[j]==0:
        flag[j]=1
        j = index[arr[j]]
      loops+=1
  print(length-loops)

for x in range(num):
  length = int(input())
  arr = list(map(int,input().strip().split()))
  handle(length, arr)