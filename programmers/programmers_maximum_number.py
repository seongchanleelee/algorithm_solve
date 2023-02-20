def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(key=lambda x: x*3, reverse=True)

    for i in range(len(numbers)):
        answer += numbers[i]

    return str(int(answer))
solution([6, 10, 2])
solution([3, 30, 34, 5, 9])