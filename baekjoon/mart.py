import random
n = random.randrange(5,10)
print(n)
arr = [[0]*n for _ in range(n)]
lst = [1,2,3]
# 숫자 123 넣기
for i in range(3):
    y = random.randrange(0, n - 1)
    x = random.randrange(0, n - 1)
    if arr[y][x] == 0:
        arr[y][x] = random.choice(lst)
        lst.remove(arr[y][x])



n2 = random.randrange(1,10)
# 4를 랜덤하게 넣기
for j in range(n2):
    for i in range(2):
        y = random.randrange(0,n-1)
        x = random.randrange(0,n-1)
        if arr[y][x] == 0:
            arr[y][x] = 4

print(arr)

















#-------------------------------------------------------------------------
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    y, x = 0, 0
    ans = 0
    for i in range(1, 4): # 1,2,3
        q = []
        q.append([y, x, 0])
        visit = [[0] * N for _ in range(N)]
        visit[y][x] = 1
        while q:
            q.sort(key=lambda x:x[2]) # [0,0,2] [1,0,1]
            ny, nx, cnt = q.pop(0)
            directy = [0, 1, 0, -1]
            directx = [1, 0, -1, 0]
            if arr[ny][nx] == i:
                ans += cnt
                y = ny
                x = nx
                break
            for j in range(4):
                dy = ny + directy[j]
                dx = nx + directx[j]
                if 0 <= dy < N and 0 <= dx < N:
                    if visit[dy][dx] == 1:
                        continue
                    if arr[dy][dx] == -1:
                        continue
                    if arr[dy][dx] == 4:
                        visit[dy][dx] = 1
                        q.append([dy, dx, cnt+2])
                    else:
                        visit[dy][dx] = 1
                        q.append([dy, dx, cnt+1])
    print(ans)


