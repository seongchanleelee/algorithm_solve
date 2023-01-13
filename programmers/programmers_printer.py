def solution(priorities, location):
    answer = 0
    arr = []
    for i in range(len(priorities)):
        arr.append(i)

    while 1:
        if priorities[0] != max(priorities):
            priorities.append(priorities.pop(0))
            arr.append(arr.pop(0))
        else:
            priorities.pop(0)
            answer += 1
            if arr.pop(0) == location:
                break

    return answer
solution([2, 1, 3, 2],2)