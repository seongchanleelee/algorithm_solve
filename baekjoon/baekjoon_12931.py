n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
cnt = 0
while arr != [0]*n:
    yn = True
    for i in range(len(arr)):
        if arr[i] %2 !=0:
            arr[i] = arr[i] -1
            cnt +=1
            yn = False
            break
    if yn == True:
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i] = arr[i]//2
        cnt +=1
print(cnt)
