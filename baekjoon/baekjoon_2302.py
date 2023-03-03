n = int(input())
dp = [0]*(n+1)
m = int(input())
arr = []
for i in range(m):
    vip = int(input())
    arr.append(vip)
result = 1
dp[0] = 1
dp[1] = 1

st = 2
for i in range(st, n+1):
        dp[i] = dp[i-1] + dp[i-2]

# 슬라이싱 하여 dp구간 나눠주기
if len(arr)>=1:
    cnt = 0
    for i in range(len(arr)):
        result *= dp[arr[i]-1-cnt]
        cnt = arr[i]
    result *= dp[n-cnt]
else:
    result = dp[n]

print(result)
