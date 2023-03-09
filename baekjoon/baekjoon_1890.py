n = int(input())
dp = [[0]*n for _ in range(n)]
arr = [list(map(int,input().split()))for _ in range(n)]

dp[0][0] = 1

for y in range(n):
    for x in range(n):
        if y == n-1 and x == n-1:
            print(dp[y][x])
            break

        if y + arr[y][x] < n:
            dp[y + arr[y][x]][x] += dp[y][x]
        if x + arr[y][x] < n:
            dp[y][x+ arr[y][x]] += dp[y][x]
# print(dp)
