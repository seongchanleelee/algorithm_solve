while 1:

    arr = list(map(int,input().split()))
    k=arr[0]
    arr=arr[1:]
    path = [0]*6
    def abc(level, start):
        if level == 6:
            print(*path)
            return

        for i in range(start,k):
            path[level] = arr[i]
            abc(level+1, i+1)
            path[level] = 0

    abc(0,0)
    print("")
    if k ==0:
        break