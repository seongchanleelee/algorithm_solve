def solution(s):
    s=s.split(' ')
    for i in range(len(s)):
        s[i] = int(s[i])
    answer = str(min(s)) + ' ' + str(max(s))

    return answer
print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
print(solution("-1 1 2 -3"))
