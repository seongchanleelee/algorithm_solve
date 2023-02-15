from collections import deque
def solution(macaron):
    answer = []
    arr = [[0]*6 for _ in range(6)]
    delete = [[0]*6 for _ in range(6)]
    def bfs(start):
        q = deque()
        q.append(start)

        directy = [-1,1,0,0]
        directx = [0,0,-1,1]
        while q:
            nowy, nowx, nowa, nowcnt = q.popleft()
            # # 마카롱 떨구기
            # if nowcnt >=3 and bool(q) == False:
            #     for y in range(6):
            #         for x in range(6):
            #             if visit[y][x] ==1:
            #                 arr[y][x] = 0
            #     for y in range(5,0,-1):
            #         for x in range(6):
            #             if arr[y][x] ==0 and arr[y-1][x]:
            #                 arr[y-1][x], arr[y][x] = arr[y][x], arr[y-1][x]

            for i in range(4):
                dy = nowy + directy[i]
                dx = nowx + directx[i]

                if 0<=dy<6 and 0<=dx<6:
                    if visit[dy][dx] ==1: continue
                    if arr[dy][dx] != nowa: continue
                    visit[dy][dx] = 1
                    q.append((dy,dx,nowa,nowcnt+1))
            # 마카롱 떨구기
            if nowcnt >= 3 and bool(q) == False:
                for y in range(6):
                    for x in range(6):
                        if visit[y][x] == 1:
                            arr[y][x] = 0
                for y in range(5, 0, -1):
                    for x in range(6):
                        if arr[y][x] == 0 and arr[y - 1][x]:
                            arr[y - 1][x], arr[y][x] = arr[y][x], arr[y - 1][x]




    for i in range(len(macaron)):
        for j in range(len(arr)-1,-1,-1):
            if arr[j][macaron[i][0]-1] ==0:
                arr[j][macaron[i][0]-1] = macaron[i][1]
                break

        # for y in range(5,-1,-1):
        #     for x in range(6):
        #         if arr[y][x] ==0 and arr[y-1][x] != 0:
        #             while 1:
        #                 arr[y-1][x] , arr[y][x] = arr[y][x], arr[y-1][x]



                if arr[y][x] !=0:
                    visit = [[0]*6 for _ in range(6)]
                    visit[y][x] = 1
                    bfs((y,x,arr[y][x],1))


    print(arr)
    return answer

solution([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]])