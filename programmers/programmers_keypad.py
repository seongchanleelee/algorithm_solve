def solution(numbers, hand):
    answer = ''
    # arr=[[1,2,3],[4,5,6],[7,8,9],[10,0,11]] *과 #을 10, 11 로 둠
    lhand = 10
    rhand = 11

    points = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 2)]
    while numbers:
        key = numbers.pop(0)

        if key in [1, 4, 7]:
            answer += "L"
            lhand = key
        elif key in [3, 6, 9]:
            answer += "R"
            rhand = key

        # key가 2,5,8,0중 하나인 경우
        else:
            lmove = abs(points[lhand][0] - points[key][0]) + abs(points[lhand][1] - points[key][1]) #
            rmove = abs(points[rhand][0] - points[key][0]) + abs(points[rhand][1] - points[key][1])

            if lmove > rmove:
                answer += "R"
                rhand = key
            elif rmove > lmove:
                answer += "L"
                lhand = key
            else:
                if hand == "right":
                    answer += "R"
                    rhand = key
                else:
                    answer += "L"
                    lhand = key

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
lhand = [1,4,7]
rhand = [3,6,9]



