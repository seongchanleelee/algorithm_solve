import sys
while 1:
    l,r,c = list(map(int,input().split())) #l: 층수 r: 행, c:열
    building = []
    visit = []
    if l==0 and r==0 and c ==0:
        break
    for i in range(l):
        arr = [list(input())for _ in range(r)]
        arr2 = [[0]*c for _ in range(r)]
        building.append(arr)
        visit.append(arr2)

    def bfs(start):
        q = []
        q.append(start)

        while q:
            nowf, nowy, nowx, nowcnt = q.pop(0)

            if arr[nowf][nowy][nowx] == "E":
                return nowcnt
            directy = [-1,1,0,0,0,0] # 상 하 좌 우 위 아래
            directx = [0,0,-1,1,0,0]
            directf = [0,0,0,0,-1,1]

            for i in range(6):
                dy = directy[i] + nowy
                dx = directx[i] + nowx
                df = directf[i] + nowf

                if 0 <=dy < r and 0<=dx< c and 0 <=df < l:
                    if visit[df][dy][dx] == 1: continue
                    if building[df][dy][dx] =="#": continue
                    visit[df][dy][dx] = 1
                    q.append((df, dy, dx, nowcnt+1))


    for f in range(l):
        for y in range(r):
            for x in range(l):
                if building[f][y][x] =="S":
                    print(bfs((f,y,x,0)))


