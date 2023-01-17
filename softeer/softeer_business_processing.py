h, k, r = list(map(int,input().split()))
lst = []
dp =[0]*11
dp[0] =1
dp[1] =2
dp[2] =4
for i in range(3,len(dp)):
    dp[i] = dp[i-1]*2
print(dp)
arr = []
for i in range(dp[h]):
    arr.append(list(map(int,input().split())))
print(arr)

left = []
right = []
for i in range(r):
















# arr = []
# cnt = 0
# for i in range(1,r+1):
#     arr.append(left.pop(0))
#     arr.append(right.pop(0))
#     if i >=2:
#         if i%2 ==0:
#             cnt+=arr[i-1]
#         else:
#             cnt+=arr[i-2]
# print(cnt)