def solution(k, d):
    answer = 0
    start = 0
    cnt = 0
    for y in range(start,d+1,k):
        if y >=1:
            start += k
        for x in range(start,d+1,k):
            if (y**2 + x**2)**0.5 > d:
                break
            if y != x:
                answer +=1
            else:
                cnt +=1
    answer *=2
    print(answer)
    print(answer + cnt)
    return answer + cnt
# solution(2,4)
# solution(1,5)


def solution(k, d):
    answer = 0
    for x in range(0, d+1, k):
        y = (d**2 - x**2)**0.5
        answer += y//k + 1
    return int(answer)
#
# def solution(k, d):
#     answer = 0
#     for i in range(0, d+1, k):
#         max_y = d*d - i*i
#         answer += int(max_y ** 0.5)//k + 1
#     return answer
# solution(2,4)
print(solution(1,5))