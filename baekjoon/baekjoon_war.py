n,m = list(map(int,input().split()))

arr = [list(input()) for _ in range(m)]
visit = [[0]*n for _ in range(m)]
w = 0
b = 0
def bfs(start):
    global visit, w, b
    q = []
    q.append(start)
    Wyes = True
    if start[2] == 'W':
        Wyes = True
    else:
        Wyes = False

    cnt = 1
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]

    while q:
        nowy, nowx, now = q.pop(0)
        for i in range(4):
            dy = nowy + directy[i]
            dx = nowx + directx[i]

            if 0<=dy<m and 0<=dx<n:
                if visit[dy][dx] == 1: continue
                if now != arr[dy][dx]: continue
                visit[dy][dx] = 1
                cnt +=1
                q.append((dy,dx,arr[dy][dx]))
    if Wyes == True:
        w += cnt**2
        return
    else:
        b += cnt**2
        return


for y in range(m):
    for x in range(n):
        if arr[y][x] =="W" and visit[y][x] == 0:
            visit[y][x] = 1
            bfs([y,x,"W"])
        if arr[y][x] =="B" and visit[y][x] ==0:
            visit[y][x] = 1
            bfs([y,x,"B"])
print(w, b)