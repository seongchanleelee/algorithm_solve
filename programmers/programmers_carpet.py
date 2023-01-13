result = []
def solution(brown, yellow):
    global result
    answer = []
    for i in range(1,brown+yellow+1):
        if int((brown + yellow) / i) == ((brown + yellow) / i):
            if ((brown + yellow) / i) <= i:
                answer.append([i, (brown+yellow)/i])

    for i in range(len(answer)):
        if (answer[i][0]-2) * (answer[i][1]-2) == yellow:
            result = [answer[i][0],int(answer[i][1])]

    return result

print(solution(10,2))

