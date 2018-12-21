num = int(input().strip())

def handle(arr1, arr2, len1, len2):
  res = ''
  for i in range(len2):
    num = arr1.count(arr2[i])
    for j in range(int(num)):
      res += str(arr2[i])
      res += ' '
    for j in range(len1):
      if arr1[j] == arr2[i]:
        arr1[j] = -1
  temp = []
  for i in range(len1):
    if arr1[i] != -1:
      temp.append(arr1[i])
  temp = sorted(temp)
  for i in range(len(temp)):
    res += str(temp[i])
    res += ' '
  print(res.strip())
  


for x in range(num):
  len1, len2 = list(map(int,input().strip().split()))
  arr1 = list(map(int,input().strip().split()))
  arr2 = list(map(int,input().strip().split()))
  handle(arr1, arr2, len1, len2)