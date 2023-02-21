def solution(numbers, target):
    answer = 0
    def dfs(level, result):
        nonlocal answer, target
        if level ==len(numbers):
            if result == target:
                answer+=1
            return

        dfs(level+1, result + numbers[level])
        dfs(level+1, result - numbers[level])

    dfs(0,0)
    return answer
print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))