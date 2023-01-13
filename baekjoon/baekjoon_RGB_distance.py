n = int(input())
arr = [list(map(int,input().split()))for _ in range(n)]
# 3개의 경우로 케이스를 나눔
dp = [[0]*3 for _ in range(n+1)]
dp[1][0] = arr[0][0]
dp[1][1] = arr[0][1]
dp[1][2] = arr[0][2]
arr = [[0,0,0]] + arr
for i in range(2,n+1):
    for j in range(3):
        if j ==0:
            dp[i][j] = min(arr[i][j] + dp[i-1][1], arr[i][j] + dp[i-1][2])

        if j ==1:
            dp[i][j] = min(arr[i][j] + dp[i - 1][0], arr[i][j] + dp[i - 1][2])

        if j ==2:
            dp[i][j] = min(arr[i][j] + dp[i - 1][1], arr[i][j] + dp[i - 1][0])

print(min(dp[-1]))
