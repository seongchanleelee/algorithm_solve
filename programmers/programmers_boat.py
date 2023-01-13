def solution(people, limit):
    answer = 0
    people.sort()
    print(people)

    start, end = 0, len(people) -1
    while start <= end:
        answer +=1
        if people[start] + people[end] <= limit:
            start +=1
        end -=1



    return answer
print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))