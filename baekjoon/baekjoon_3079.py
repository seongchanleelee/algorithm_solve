n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

st = 0
ed = m * max(arr)

result = 0
while st <= ed:
    mid = int((st + ed))//2
    cnt = 0
    for i in range(len(arr)):
        cnt += mid // arr[i]
    # cnt가 많다면
    if cnt >= m:
        ed = mid -1
        result = mid

    # cnt 가 적다면
    if cnt <m:
        st = mid +1
print(result)