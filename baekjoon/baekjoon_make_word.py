from itertools import permutations
n = int(input())
for _ in range(n):
    arr = input()
    a = [''.join(p) for p in permutations(arr)]
    a = set(a)
    a = list(a)
    a.sort()


    for i in range(len(a)):
        if a[i] == arr:
            if i == len(a)-1:
                print(a[i])
                break
            else:
                print(a[i+1])
                break
###################################################################
n = int(input())
for _ in range(n):
    arr = list(input())
    lst = []
    result = []
    cnt = 0

    for i in range(len(arr)-1,0,-1):
        if ord(arr[i]) > ord(arr[i-1]):
            cnt+=1

            for j in range(0,i-1):
                result.append(arr[j])

            for j in range(i-1,len(arr)):
                lst.append(arr[j])

            lst.sort()
            for j in range(len(lst)):
                if lst[j] > arr[i-1]:
                    result.append(lst[j])
                    lst.remove(lst[j])
                    result= result + lst
                    break
            break
    if cnt ==0:
        result = arr

    for i in range(len(result)):
        print(result[i],end='')
    print()









