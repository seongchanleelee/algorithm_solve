#1 -> out
#0 -> in

# 한번 -> 1개
# 2 늘어남
# 두번 -> 3개
# 4늘어남
# 세번 -> 7개
# 8늘어남
# 4번 -> 15개
# (11*2) + 15 37 늘어남

# 2 대 1 가능
# 4 대 3 가능
# 증가폭대로 가능 함 -> 같은 숫자가 증가폭 까진 가능하다는 뜻
t = int(input())
for tc in range(t):
    arr = list(input())
    # print(arr)
    dp = [0]*((len(arr) //2) +1)
    if len(dp) <=2:
        dp = [0,1,3]
    else:
        dp[0] = 1
        dp[1] = 1
        dp[2] = 3
    if len(dp) >=3:
        for i in range(3,len(dp)):
            dp[i] = 2*(dp[i-1] -dp[i-2]) + dp[i-1]
    # print(dp)
    in_out = [0]*2
    for i in range(len(arr)):
        if arr[i] == '0':
            in_out[0] +=1
        else:
            in_out[1] +=1
    flag = True
    if len(arr)//2 !=0:
        for i in range(len(in_out)):
            # print(dp[len(arr) //2] - dp[len(arr)//2 -1])
            if in_out[i] > dp[len(arr) //2] - dp[len(arr)//2 -1]:
                flag = False
    if flag == False:
        print('NO')
    else:
        print('YES')


