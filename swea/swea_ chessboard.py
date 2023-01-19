t = int(input())
for tc in range(1, t+1):
    arr = [list(input())for _ in range(8)]

    yn = "yes"
    cnt = 0
    for y in range(len(arr)):
        cnt2 = 0
        for x in range(len(arr[y])):
            if arr[y][x] =="O":
                cnt +=1
                cnt2 +=1

                for i in range(8):
                    if arr[i][x] =="O" and i != y:
                        yn = "no"
        if cnt2 >=2:
            yn = "no"
    if cnt !=8:
        yn = "no"

    print(f"#{tc} {yn}")
