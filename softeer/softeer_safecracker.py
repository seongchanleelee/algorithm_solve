W,N = list(map(int,input().split()))
arr = []
for i in range(N):
    lst = list(map(int,input().split()))
    arr.append(lst)
arr.sort(key=lambda x: x[1], reverse=True)

answer = 0
for i in range(N):
    if W >= arr[i][0]:
        answer += (arr[i][0]*arr[i][1])
        W -= arr[i][0]
    else:
        answer += arr[i][1] * W
        break
print(answer)