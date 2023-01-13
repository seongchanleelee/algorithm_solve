def solution(land):
    for y in range(1, len(land)): #두번째 줄 부터 경우를 탐색하며 내려옴
        for x in range(4): # 4개 열중 전에 탐색한 열은 제외하며 최댓값을 구함
            land[y][x] += max(land[y-1][:x] + land[y-1][x+1:])
    return max(land[len(land)-1])
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))