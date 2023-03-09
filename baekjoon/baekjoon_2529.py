k = int(input())
arr = list(input().split())
num = [0,1,2,3,4,5,6,7,8,9]
visit = [0]*10
path = [0]*(k+1)
result = []
def dfs(level):
    global path, result
    if level == k+1:
        check = [0]*k
        for i in range(len(path)-1):
            if path[i] < path[i+1] and arr[i] == '<':
                check[i] = 1
            if path[i] > path[i+1] and arr[i] == '>':
                check[i] = 1
        if check == [1]*k:
            p = ''
            for j in range(len(path)):
                p += str(path[j])
            result.append(p)

        return

    for i in range(len(num)):
        if visit[i] ==1: continue
        visit[i] = 1
        path[level] = num[i]
        dfs(level+1)
        visit[i] = 0
        path[level] = 0
dfs(0)
result.sort()
print(result[-1])
print(result[0])