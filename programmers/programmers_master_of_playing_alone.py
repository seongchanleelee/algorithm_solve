def solution(cards):
    answer = 0
    visit = [0] * len(cards)
    arr = []
    Max = 0
    Max2 = 0
    for i in range(len(cards)):
        if arr ==[]:
            arr.append(cards[i])
            visit[i] = 1
        while 1:
            if visit[arr[-1]-1] ==0:
                visit[arr[-1] - 1] = 1
                arr.append(cards[arr[-1]-1])
            else:
                Max = max(Max, len(arr))

                Max2 = max(Max2, len(arr))
                arr = []
                break
                # visit[arr[-1]-1] =1
    return answer

solution([8,6,3,7,2,5,1,4])