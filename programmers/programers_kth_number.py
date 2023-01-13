commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]] #i j k
array = [1, 5, 2, 6, 3, 7, 4]

def solution(array, commands):
    answer = []
    for y in range(len(commands)):
        result = []
        # for x in range(len(commands[y])):
        i=commands[y][0]
        j = commands[y][1]
        k = commands[y][2]

        for a in range(i-1,j):
            result.append(array[a])
        result.sort()
        ans=result[k-1]

        answer.append(ans)
    return answer

print(solution(array,commands))