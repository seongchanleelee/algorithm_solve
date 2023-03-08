def dfs(level, path):
    global Max
    if level ==11:
        Max = max(sum(path), Max)
        return

    for i in range(len(arr[level])):
        if arr[level][i] == 0: continue
        if visit[i] == 1: continue
        visit[i] = 1
        dfs(level+1, path + [arr[level][i]])
        visit[i] = 0

t = int(input())
for tc in range(t):
    arr = [list(map(int,input().split()))for _ in range(11)]
    Max = 0
    visit = [0]*11
    dfs(0,[])
    print(Max)