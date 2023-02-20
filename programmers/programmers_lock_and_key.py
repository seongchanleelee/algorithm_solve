# lock 에 0이 있는부분을 n*n 처리 해주기
# key를 돌려서 n*n으로 탐색하며 lock의 홈 부분이랑 맞는게 있는지 확인
# 있다면 true, 없다면 false
# 단 열쇠의 돌기와 자물쇠의 돌기가 만나면 안됨!

def solution(key, lock):
    answer = True
    arry = []
    arrx = []
    arr = []
    for y in range(len(lock)):
        for x in range(len(lock[y])):
            if lock[y][x] ==0:
                arry.append(y)
                arrx.append(x)
                arr.append((y,x))
    ny = max(arry) - min(arry) +1
    nx = max(arrx) - min(arrx) +1
    n = max(ny, nx)
    lockk = [[1]*n for _ in range(n)]
    hom = 0
    for i in range(len(arr)):
        lockk[n - arr[i][0]-1][n - arr[i][1]-1] = 0
        hom +=1
    print(lockk)
    directy = []
    directx = []
    for i in range(n):
        # direct 배열을 n*n 으로 만들어서 완탐해보기
        for j in range(n):
            directy.append(i)
            directx.append(j)


    # 90 180 270 360 돌리고 direct 배열로 확인하기
    # 뒤집기
    for i in range(4):
        newkey = []
        for y in range(len(key)):
            newarr = []
            for x in range(len(key)-1,-1,-1):
                newarr.append(key[x][y])
            newkey.append(newarr)


        key = newkey


        for y in range(len(key)):
            for x in range(len(key[y])):
                cnt = 0
                for i in range(n*n):
                    dy = directy[i] + y
                    dx = directx[i] + x

                    if 0<=dy<len(key) and 0<=dx<len(key[0]):
                        # print(lockk[directy[i]][directx[i]])
                        if key[dy][dx] == 1 and lockk[directy[i]][directx[i]] ==0:
                            cnt +=1
                        elif key[dy][dx] ==1 and lockk[directy[i]][directx[i]] ==1:
                            cnt = 0
                if cnt == hom:
                    answer = True
                    return answer
                else:
                    answer = False
        return answer
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 0], [0, 1]]))