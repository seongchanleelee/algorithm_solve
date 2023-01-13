def solution(nums):
    answer = 0
    choice = int(len(nums)//2)
    d = list(set(nums))

    if len(d) >=choice:
        answer = choice
    else:
        answer = int(len(d))
    return answer
solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])