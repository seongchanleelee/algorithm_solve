# dp리스트는 각 index에 최대 점수가 들어감

n = int(input())
arr = [int(input()) for _ in range(n)]
# dp란 리스트는 해당위치 최댓값을 뜻함
dp = [0]*n
if len(arr) <=2:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2,n):
        case1 = dp[i-3] + arr[i-1] + arr[i] # 지금위치에 한 계단을 건너고 온 경우
        case2 = dp[i-2] + arr[i] # 지금위치에 두 계단을 건너고 온 경우
        dp[i] = max(case1, case2)
    print(dp[-1])
