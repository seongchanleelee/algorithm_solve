def bfs(start):
    q = []
    q.append(start)
    arr[y][x] = "."
    directy = [-1, 1, 0, 0]
    directx = [0, 0, -1, 1]
    while q:
        nowy, nowx = q.pop(0)

        for i in range(4):
            dy = directy[i] + nowy
            dx = directx[i] + nowx

            if 0<=dy<H and 0<=dx<W :
                if arr[dy][dx] ==".": continue
                if arr[dy][dx] =="#":
                    q.append((dy,dx))
                    arr[dy][dx] = "."


t = int(input())
for tc in range(t):
    H,W = list(map(int,input().split()))
    arr=[list(input()) for _ in range(H)]
    answer = 0
    for y in range(H):
        for x in range(W):
            if arr[y][x] =="#":
                arr[y][x] = "."
                bfs((y,x))
                answer += 1
    print(answer)