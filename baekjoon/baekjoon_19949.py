arr = list(map(int,input().split()))
path = [0]*10
num = [0,1,2,3,4,5]
used = [0,0,0,0,0,0]
result = 0
def dfs(level):
    global result

    if level ==10:
        cnt = 0
        for i in range(len(path)):
            if path[i] == arr[i]:
                cnt +=1
                if cnt >=5:
                    break
        if cnt >=5:
            result +=1
        return

    for i in range(1, len(used)):
        if level >1 and (path[level-2] == path[level-1] and path[level-1] == i):
            continue
        path[level] = num[i]
        dfs(level+1)
        path[level] = 0

dfs(0)
print(result)