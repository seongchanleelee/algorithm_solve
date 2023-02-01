n,m = list(map(int,input().split())) #n: 집의 수, m: 다리의 수
s,e = list(map(int,input().split())) #s:숭이 위치, e: 혜빈이 위치
arr = []
for i in range(m):
    arr.append(list(map(int,input().split())))

print(arr)
arr.sort()
print(arr)
lst = [[0]*(n+1) for _ in range(n+1)]
inf = 21e8

for i in range(m):
    lst[arr[i][0]][arr[i][1]] = arr[i][2]
print(lst)

for i in range(1,n+1):
    for j in range(1,n+1):
        if not lst[i][j]:
            lst[i][j] = inf

for i in range(1,n+1):
    lst[i][i] = 0

used = [0]*(n+1)
result = lst[s][:]
used[s] = 1

for i in range(n):
    via_min = inf
    via = 0
    for j in range(1,n+1):
        if not used[j] and result[j] < via_min:
            via = j
            via_min = result[j]
    used[via] = 1
    for j in range(1,n+1):
        if result[j] > result[via] + lst[via][j]:
            result[j] = result[via] + lst[via][j]
print(result)


