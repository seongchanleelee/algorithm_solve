citations = [3, 0, 6, 1, 5]

def solution(citations):
    answer = 0
    for i in citations:     # 모든 숫자 탐색
        cnt = 0
        for j in range(len(citations)):        # 해당 숫자에서 인용 횟수 확인
            if i <= citations[j]:
                cnt += 1
        if i >= cnt:            # 논문이 인용된 횟수가 h번 이상
            if answer < cnt:    # max값 확인
                answer = cnt    # 논문이 몇편 인용되어있는지가 cnt
    return answer

print(solution(citations))

#---------------------------------------------
citations = [3,0,6,1,5]
# citations = [8,0,4,2,5,13,9]

def solution(citations):
    citations.sort()

    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            return len(citations) - i
            # break

    # return None
    return 0

print(solution(citations))