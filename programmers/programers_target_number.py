numbers = [1, 1, 1, 1, 1]
target = 3
arr = ['-','+']
used = [0]*len(numbers)
cnt = 0

def dfs(level,Sum):
    global cnt
    if level == len(numbers):
        if Sum == target:
            cnt+=1
        return

    for i in range(2):
        if arr[i] =='-':
            if used[level] == 1: continue
            used[level] = 1
            dfs(level+1,Sum-numbers[level])
            used[level] = 0
        if arr[i] =='+':
            if used[level] ==1: continue
            used[level] = 1
            dfs(level+1, Sum+numbers[level])
            used[level] = 0

dfs(0,0)
# print(cnt)


def solution(numbers, target):
    answer = 0
    arr = ['-', '+']
    used = [0] * len(numbers)

    def dfs(level, Sum):
        nonlocal answer
        if level == len(numbers):
            if Sum == target:
                answer += 1
            return

        for i in range(2):
            if arr[i] == '-':
                dfs(level + 1, Sum - numbers[level])

            if arr[i] == '+':
                dfs(level + 1, Sum + numbers[level])


    dfs(0, 0)

    return answer

print(solution([1, 1, 1, 1, 1], 3))