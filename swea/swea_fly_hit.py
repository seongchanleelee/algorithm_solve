def bfs(start):
    global Max
    cnt = 0
    nowy, nowx = start[0], start[1]
    for i in range(m**2):
        dy = directy[i] + nowy
        dx = directx[i] + nowx

        if 0<=dy<n and 0<=dx<n:
            cnt += arr[dy][dx]
    Max = max(Max,cnt)
    return

t = int(input())
for tc in range(1,t+1):
    n, m = list(map(int,input().split()))
    arr = [list(map(int,input().split()))for _ in range(n)]
    Max = 0
    directy = []
    directx = []

    for i in range(m):
        directy += [i] * m

    for i in range(m):
        for j in range(m):
            directx.append(j)

    for y in range(n):
        for x in range(n):
            bfs((y, x))
    print(f"#{tc} {Max}")

