def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            pass
        else:
            answer.append(arr[i])
    answer.append(arr[-1])
    return answer
solution([1,1,3,3,0,1,1])
solution([4,4,4,3,3])