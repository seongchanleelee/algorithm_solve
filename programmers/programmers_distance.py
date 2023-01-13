def solution(places):
    # bfs코드#######################################
    def bfs(start):
        q = []
        q.append(start)
        directy = [-1,1,0,0]
        directx = [0,0,-1,1]
        result = 1
        while q:
            nowy, nowx, cnt = q.pop(0)
            if cnt >=2:
                continue
            for i in range(4):
                dy = directy[i] + nowy
                dx = directx[i] + nowx

                if 0<=dy<5 and 0<=dx<5:
                    if arr[dy][dx] != "P" and cnt <2 and visit[dy][dx] != 1:
                        visit[dy][dx] = 1
                        # 중간에 X 가 나온다면 괜찮음
                        if arr[dy][dx] =="X":
                            continue
                        q.append((dy,dx,cnt+1))
                    # 맨허튼 거리안에 P가 있다면 0이 들어가게끔 함
                    elif arr[dy][dx] =="P" and visit[dy][dx] ==0 and cnt <2:
                        result = 0
        return result
    ######################################################################
    answer = []
    # 문자열을 빈 리스트에 넣어서 정리해줌 (bfs를 하기 위한 작업)
    for i in range(len(places)): #경우
        arr = []

        a = 1
        for y in range(len(places[i])):
            lst = []
            for x in range(len(places[i][y])):
                lst.append(places[i][y][x])
            arr.append(lst)
        #bfs시작
        for y in range(len(arr)):
            for x in range(len(arr[y])):
                if arr[y][x] == "P":
                    visit = [[0] * 5 for _ in range(5)]
                    visit[y][x] = 1
                    # bfs시작
                    posible=bfs((y,x,0))
                    # 하나라도 거리두기가 안되면 answer에 0을 추가하기 위해 a를 0으로 바꿈
                    if posible ==0:
                        a = 0
        # a라는 전역변수로 answer에 넣어줌
        answer.append(a)
    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
# 맨해튼 거리 abs(y2-y1) + abs(x2-x1)