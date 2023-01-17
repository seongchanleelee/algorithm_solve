import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))

ave = []
for i in range(n):
    ave.append(list(map(int,input().split())))

arr = []
for i in range(m):
    arr.append(list(map(int,input().split())))

lst = [0]*100
st = 0
for i in range(len(ave)):
    for j in range(st,st+ave[i][0]):
        if j == st + ave[i][0] -1:
            st +=ave[i][0]
        lst[j] = ave[i][1]

lst2 = [0]*100
st = 0
for i in range(len(arr)):
    for j in range(st, st+arr[i][0]):
        if j == st + arr[i][0] -1:
            st += arr[i][0]
        lst2[j] = arr[i][1]

Max = 0
for i in range(100):
    if lst2[i] > lst[i]:
        Max = max(Max, lst2[i] - lst[i])
print(Max)