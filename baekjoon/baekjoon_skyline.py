n = int(input())
visited = [0]
cnt = 0
for tc in range(n):
    x, y = list(map(int,input().split()))
    if y > visited[-1]:
        cnt += 1
        visited.append(y)

    else:
        while y < visited[-1]:
            visited.pop()

        if y > visited[-1]:
            cnt += 1
            visited.append(y)
print(cnt)
