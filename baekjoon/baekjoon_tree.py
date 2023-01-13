def dfs(d): # 자를 노드를 확인후 하단에 리프노드도 다 예외시켜줌
    arr[d] = -2
    for i in range(n):
        if d == arr[i]:
            dfs(i)

n = int(input())
arr = list(map(int,input().split()))
d = int(input())
cnt = 0
dfs(d)

for i in range(n):
    if arr[i] != -2 and i not in arr: #잘린 노드에 포함되지 않거나, 리프노드 일시
        cnt+=1
print(cnt)
