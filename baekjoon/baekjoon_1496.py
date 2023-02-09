import sys
input = sys.stdin.readline
n, s, m = list(map(int,input().split()))
arr = list(map(int,input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1,n+1):
    for j in range(m+1):
        if dp[i-1][j] !=0:
            if 0<= j + arr[i-1] <=m:
                dp[i][j+arr[i-1]] = 1
            if 0<=j - arr[i-1] <=m:
                dp[i][j-arr[i-1]] = 1

result = -1
for i in range(m,-1,-1):
    if dp[n][i] ==1:
        result = i
        break
print(result)