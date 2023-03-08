import sys

input = sys.stdin.readline

N = int(input())

cost = []

for _ in range(N):
    price = list(map(int, input().split()))
    cost.append([price[0], price[1]])

cost.sort(key = lambda x: (x[0], x[1]))

total = [0] * N

for i in range(N):
    for j in range(i, N):
        benefit = cost[i][0] - cost[j][1]
        if benefit > 0:
            total[i] += benefit
result = [cost[i][0] for i in range(N) if total[i] == max(total)]

if sum(total) == 0:
    print(0)
else:
    print(min(result))