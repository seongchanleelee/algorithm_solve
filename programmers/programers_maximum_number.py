numbers1 = [[6, 10, 2], [3, 30, 34, 5, 9]]

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    return str(int(answer))

for i in range(len(numbers1)):
    numbers= numbers1[i]
    print(solution(numbers))
