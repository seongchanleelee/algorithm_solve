arr = [list(input()) for _ in range(5)]
Max = 0
for i in range(len(arr)):
    Max = max(len(arr[i]), Max)

for i in range(len(arr)):
    if len(arr[i]) != Max:
        arr[i] += ['_']*(Max - len(arr[i]))

S = ''
for x in range(len(arr[0])):
    for y in range(len(arr)):
        if arr[y][x] !="_":
            S += arr[y][x]
print(S)