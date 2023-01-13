def solution(progresses, speeds):
    answer = []
    cnt = 0 # 개발일수
    cnt2 = 0 # 한 프로그레스의 전체개발일수
    result = 1 #한번에 몇개의 프로그래스를 제출 하는지
    for i in range(len(progresses)):
        while progresses[i] < 100:
            progresses[i] +=speeds[i]
            cnt +=1
        if cnt2 ==0:
            cnt2 = cnt
            cnt = 0
        else:
            if cnt2 >= cnt:
                result +=1
            else:
                answer.append(result)
                cnt2 = cnt
                result = 1
            cnt = 0
    answer.append(result)
    return answer
print(solution([93, 30, 55], 	[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1] ))