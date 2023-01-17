n = int(input())
arr = [list(map(int,input())) for _ in range(n)]
# print(arr)
from collections import deque
def bfs(start):
    global cnt
    q = deque()
    q.append(start)

    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]

            if 0<=dy<n and 0<=dx<n:
                if visit[dy][dx] ==1: continue
                if arr[dy][dx] ==0: continue
                visit[dy][dx] = 1
                cnt+=1
                q.append((dy,dx))



    return
lst = []
visit = [[0]*n for _ in range(n)]
for y in range(n):
    for x in range(n):
        cnt = 0
        if arr[y][x] ==1:
            if visit[y][x] ==1: continue
            visit[y][x] = 1
            cnt +=1
            bfs((y,x))
            lst.append(cnt)
print(len(lst))
lst.sort()
# print(visit)
for i in lst:
    print(i)
