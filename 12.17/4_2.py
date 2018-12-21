def getCount(arr):
    i=0
    c=0
    while i<len(arr):
        j=i+1
        while j<len(arr):
            if arr[i]>arr[j]:
                c+=1
            j+=1
        i+=1
    return c

num1 = int(input(''))
i=1
while i<=num1:
    num2 = int(input(''))
    str_in = input('') #输入数组
    arr = [int(num2) for num2 in str_in.split()]
    res=getCount(arr)
    print(res)
    i+=1