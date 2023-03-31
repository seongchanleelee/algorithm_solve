from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visit = [[0]*m for _ in range(n)]
    directy = [-1,1,0,0]
    directx = [0,0,-1,1]
    def bfs(start):
        q = deque()
        q.append(start)

        while q:
            nowy, nowx, nowcnt = q.popleft()

            for i in range(4):
                dy = nowy + directy[i]
                dx = nowx + directx[i]

                if 0<=dy<len(maps) and 0<=dx<len(maps[0]):
                    if maps[dy][dx] == 0: continue
                    if visit[dy][dx] == 1: continue
                    if [dy, dx] == [len(maps)-1, len(maps[0])-1]:
                        return nowcnt +1
                    visit[dy][dx] =1
                    q.append((dy,dx,nowcnt +1))





    answer = bfs((0,0,1))

    if answer == None:
        answer = -1

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))