n=int(input())
arr=list(map(int, input().split()))
result = [1]*n
result[0] = arr[0]
for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            result[i] =max(result[i],result[j] + arr[i])
        else:
            result[i] = max(result[i], arr[i])
print(max(result))
