def solution(k, tangerine):
    answer = 0
    dic = {}
    for i in range(len(tangerine)):
        if tangerine[i] in dic:
            dic[tangerine[i]] += 1
        else:
            dic[tangerine[i]] = 1

    dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse= True))

    for i in dic:
        if k <=0:
            return answer
        k -=dic[i]
        answer +=1

    return answer

solution(6, [1, 3, 2, 5, 4, 5, 2, 3])
solution(4, [1, 3, 2, 5, 4, 5, 2, 3])
solution(2, [1, 1, 1, 1, 2, 2, 2, 3])