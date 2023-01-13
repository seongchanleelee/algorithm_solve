n,m = map(int,input().split())
arr = [[0]*(m+1) for _ in range(n+1)]

arr[1][1] = 1
for y in range(1,n+1):
    for x in range(1,m+1):
        if x==1 and y==1:continue
        arr[y][x] = arr[y][x-1]+arr[y-1][x]+arr[y-1][x-1]

print(arr[n][m]%1000000007)
