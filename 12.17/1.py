num = int(input().strip())

def handle(length, arr):
  a = [0] * 61
  res = ''
  for i in range(length):
    a[arr[i]] += 1
  for i in range(length):
    max_value = max(a)
    if max_value == 0:
     break
    max_index = a.index(max_value)
    for j in range(max_value):
      res += str(max_index)
      res += ' '
    a[max_index] = 0
  print(res.strip())
  


for x in range(num):
  length = int(input())
  arr = list(map(int,input().strip().split()))
  handle(length, arr)