n = int(input())

if n>=3:
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
else:
    dp = [0,1,2]

if n >=3:
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
print((dp[-1])%10007)