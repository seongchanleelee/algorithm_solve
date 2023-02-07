def bfs(start):
    global k, v
    q = deque()
    q.append(start)
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    while q:
        nowy,nowx =q.popleft()

        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx

            if 0<=dy<r and 0<=dx<c:
                if visit[dy][dx] ==1: continue
                visit[dy][dx] = 1
                if arr[dy][dx] =='#': continue
                if arr[dy][dx] =='k':
                    k +=1
                if arr[dy][dx] =='v':
                    v +=1
                q.append((dy,dx))

from collections import deque
r,c = list(map(int,input().split()))
arr = [list(input()) for _ in range(r)]
visit = [[0]*c for _ in range(r)]
lst = [0,0]
for y in range(r):
    for x in range(c):
        if arr[y][x] =="k":
            if visit[y][x] ==1: continue
            visit[y][x] = 1
            k = 1
            v = 0
            bfs((y,x))
            if k > v:
                v = 0
            else:
                k = 0
            lst[0] += k
            lst[1] += v
        elif arr[y][x] =="v":
            if visit[y][x] ==1: continue
            visit[y][x] = 1
            k = 0
            v = 1
            bfs((y,x))
            if k > v:
                v = 0
            else:
                k = 0
            lst[0] += k
            lst[1] += v
print(*lst)
