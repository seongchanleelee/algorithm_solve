n,m = list(map(int,input().split()))
arr = [0]*n
for i in range(n):
    arr[i] = int(input())

st = min(arr)
ed = sum(arr)

while st <= ed:
    mid = (st + ed)//2

    k = 0 # 지불해야 하는 금액
    cnt = 1
    for i in range(n):
        if mid - (k+arr[i]) >=0:
            k += arr[i]
            continue
        else:
            cnt+=1
            k = arr[i]
    # m번보다 더 많이 인출하거나 인출금액이 하루의 사용금액보다 더 적은경우
    if cnt > m or mid < max(arr):
        st = mid +1
    else:
        ed = mid -1
        l = mid

print(l)


