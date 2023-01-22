t = int(input())
for tc in range(1,t+1):
    n,k = list(map(int,input().split()))
    arr = [list(map(int,input().split()))for _ in range(n)]
    answer = 0

    # 가로로 탐색
    for y in range(n):
        cnt = 0
        for x in range(n):
            if arr[y][x] ==0:
                if cnt ==k:
                    answer +=1
                cnt =0
                continue
            else:
                cnt +=1
        if cnt ==k:
            answer +=1

    #세로로 탐색
    for x in range(n):
        cnt = 0
        for y in range(n):
            if arr[y][x] ==0:
                if cnt ==k:
                    answer +=1
                cnt = 0
                continue
            else:
                cnt +=1
        if cnt ==k:
            answer +=1
    print(f"#{tc} {answer}")