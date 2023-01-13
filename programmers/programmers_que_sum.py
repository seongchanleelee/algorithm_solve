from collections import deque
def solution(queue1, queue2):
    answer = -1
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    a=sum(queue1)
    b=sum(queue2)
    c=len(queue1)*3
    cnt = 0
    while (queue1 and queue2)and c!=cnt:
        if a == b:
            return cnt

        elif a > b:
            aqpop=queue1.popleft()
            queue2.append(aqpop)
            a -= aqpop
            b += aqpop

        else:
            bqpop=queue2.popleft()
            queue1.append(bqpop)
            b -= bqpop
            a += bqpop
        cnt+=1
    return answer
print(solution([3,2,7,2],[4,6,5,1]))
print(solution([1,2,1,2],[1,10,1,2]))
print(solution([1,1],[1,5]))