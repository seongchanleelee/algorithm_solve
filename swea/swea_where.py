t = int(input())
for tc in range(1,t+1):
    n,k = list(map(int,input().split()))
    arr = [list(map(int,input().split()))for _ in range(n)]
    answer = 0
    # 가로로 확인
    cnt = 0
    for y in range(len(arr)):
        if cnt ==k:
            answer +=1
            cnt = 0
        for x in range(len(arr[y])):
            if arr[y][x] ==1:
                cnt+=1
            else:
                if cnt ==k:
                    answer +=1

                cnt = 0
            if cnt == k:
                answer +=1
                cnt = 0
    cnt = 0
    for x in range(len(arr[0])):
        if cnt ==k:
            answer +=1
            cnt = 0
        for y in range(len(arr)):
            if arr[y][x] ==1:
                cnt +=1
            else:
                if cnt ==k:
                    answer +=1
                cnt = 0
            # if cnt ==k:
            #     answer +=1
            #     cnt =0

    print(f"#{tc} {answer}")