def solution(clothes):
    answer = 1
    dic = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in dic:
            dic[clothes[i][1]] = [clothes[i][0]]
        else:
            dic[clothes[i][1]].append(clothes[i][0])

    for i in dic:
        answer *= len(dic[i]) +1
    answer -=1


    return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])