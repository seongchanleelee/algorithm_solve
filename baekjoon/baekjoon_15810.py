n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))

st = 0
ed = max(arr) * m
result = 0
while st <= ed:
    mid = (st + ed)//2
    cnt = 0
    for i in range(len(arr)):
        cnt += mid // arr[i]
    if cnt >= m:
        ed = mid -1
        result = mid
    else:
        st = mid + 1
print(int(result))