t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    dp = [[0]*15 for _ in range(k+1)]
    for i in range(15):
        dp[0][i] +=i
    for j in range(1,k+1):
        for x in range(n+1):
            for l in range(x+1):
                dp[j][x] += dp[j-1][l]
    print(dp[k][n])




