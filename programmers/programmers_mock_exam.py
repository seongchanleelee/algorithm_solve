def solution(answers):
    answer = []
    man1 = [1, 2, 3, 4, 5] *10000
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]*10000
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*10000
    cnt = [0, 0, 0, 0]
    for i in range(len(answers)):
        if man1[i] == answers[i]:
            cnt[1] += 1

        if man2[i] == answers[i]:
            cnt[2] += 1

        if man3[i] == answers[i]:
            cnt[3] += 1

    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            answer.append(i)
    return answer
print(solution([1,2,3,4,5]))