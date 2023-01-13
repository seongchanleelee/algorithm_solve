import sys
input = sys.stdin.readline

n = int(input())

arr = [0,1,1] + [0]*(n-2)
if n >=3:
    for i in range(3,n+1):
        arr[i] = arr[i-1] + arr[i-2]
print(arr[n])