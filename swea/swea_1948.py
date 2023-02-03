t = int(input())
for tc in range(1,t+1):
    year = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    nowM, nowD, nextM, nextD = list(map(int,input().split()))
    result = 0
    if nowM != nextM:
        a = year[nowM:nextM]
        result += sum(a)

    result-= nowD-1
    result+= nextD
    print(f"#{tc} {result}")