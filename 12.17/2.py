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
  # print(index)
  for i in range(length):
    if arr[i] == arr_s[i]:
      continue
    print('+++++++++++++++++')
    print(i, '----> ',arr)
    # print('swap;;;',arr[i],arr[index[arr[i]]])
    temp = arr[i]
    arr[i] = arr[int(index[temp])]
    arr[int(index[temp])] = temp
    # print(i, '----> ',arr)
    print(i, '----> ',arr)
    # arr[i], arr[index[arr[i]]] = arr[index[arr[i]]], arr[i]
    res += 1
  print(res)

for x in range(num):
  length = int(input())
  arr = list(map(int,input().strip().split()))
  handle(length, arr)