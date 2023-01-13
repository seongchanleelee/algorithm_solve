k,n = list(map(int,input().split()))
arr = []
for _ in range(k):
    arr.append(int(input()))
st = 1
ed = max(arr)
while st <= ed:
    mid = (st+ed)//2
    cnt = 0
    for i in range(k):
        lan = arr[i]
        # lan
        cnt+=lan //mid
    if cnt >= n:
        st = mid +1
    else:
        ed = mid-1
print(ed)



