N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

# 가장 높은 기둥의 크기와 index 찾기
maxI, maxV = 0, 0
for i in range(N):
    if maxV < arr[i][1]:
        maxV = arr[i][1]
        maxI = i

# 앞에서부터 가장 높은 기둥 전까지의 넓이 구하기
answer = 0
start = arr[0]
for i in range(maxI + 1):
    if i == maxI:
        answer += (arr[i][0] - start[0]) * start[1]
        answer += arr[i][1]  # 가장 높은 기둥의 넓이를 더한다.

    elif start[1] < arr[i][1]:
        answer += (arr[i][0] - start[0]) * start[1]
        start = arr[i]

# 뒤에서부터 가장 높은 기둥 전까지의 넓이 구하기
start = arr[-1]
for i in range(N - 1, maxI - 1, -1):
    if i == maxI:
        answer += (start[0] - arr[i][0]) * start[1]

    elif start[1] < arr[i][1]:
        answer += (start[0] - arr[i][0]) * start[1]
        start = arr[i]

print(answer)