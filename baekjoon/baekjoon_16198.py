n = int(input())
arr = list(map(int,input().split()))
Max = 0
lst = []

def dfs(level):
    global Max
    if len(arr) ==2:
        if Max < level:
            Max = level
        return

    if len(arr) >=3:
        for i in range(1,len(arr)-1):
            energy = arr[i-1] * arr[i+1]

            now = arr.pop(i)
            dfs(level + energy)
            arr.insert(i,now)
dfs(0)
print(Max)


