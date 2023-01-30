t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = []
    for i in range(n):
        lst = list(map(int,input().split()))
        arr.append(lst)

    # 90도
    answer90 = []
    for y in range(n):
        ans90 = []
        for x in range(n-1,-1,-1):
            ans90.append(arr[x][y])
        answer90.append(ans90)

    #180도
    answer180 = []
    for y in range(n-1,-1,-1):
        ans180 = []
        for x in range(n-1,-1,-1):
            ans180.append(arr[y][x])
        answer180.append(ans180)

    #270도
    answer270 = []
    for y in range(n-1,-1,-1):
        ans270 = []
        for x in range(n):
            ans270.append(arr[x][y])
        answer270.append(ans270)
    # 출력
    print(f'#{tc}')
    for y in range(n):
        for x in range(n):
            if x ==n-1:
                print(answer90[y][x], end=' ')
            else:
                print(answer90[y][x], end='')

        for x in range(n):
            if x ==n-1:
                print(answer180[y][x], end=' ')
            else:
                print(answer180[y][x], end='')

        for x in range(n):
            if x ==n-1:
                print(answer270[y][x])
            else:
                print(answer270[y][x], end='')
