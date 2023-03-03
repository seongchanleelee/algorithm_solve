n = int(input())

arr = [list(map(int,input().split()))for _ in range(n)]
print(arr)

lst = [0]*n
for y in range(n-1,-1,-1):
