n = int(input())
arr = [[0]*(n+1)for _ in range(n+1)]
f, c = list(map(int,input().split()))
m = int(input())
# 2중배열로 만들어줌
for i in range(m):
    x,y = map(int,input().split())
    arr[y][x] = 1
    arr[x][y] = 1

answer = -1
visit = [[0]*(n+1)for _ in range(n+1)]
def dfs(level,f):
    global answer
    if f == c:
        answer = level
        return

    for i in range(n+1):

        if arr[f][i] == 1:
            if visit[f][i] == 1: continue
            visit[f][i] = 1
            visit[i][f] = 1
            dfs(level+1,i)

dfs(0,f)
print(answer)
