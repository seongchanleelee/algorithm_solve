import heapq
def solution(jobs):
    # answer = 0
    heap = []
    start = -1
    answer, now, i = 0,0,0

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        print(heap)
        if len(heap) >0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]

            answer += now - cur[1]
            i +=1
        else:
            now +=1
    return answer // len(jobs)
print(solution([[0, 3], [1, 9], [2, 6]]))