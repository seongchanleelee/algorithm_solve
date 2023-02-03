t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = []
    for i in range(n):
        s,n = list(input().split())
        n = int(n)
        for j in range(n):
            arr.append(s)
    cnt = 0
    print(f"#{tc}")
    for i in range(len(arr)):
        cnt +=1
        if cnt ==10:
            print(arr[i])
            cnt = 0

        elif cnt != 10:
            if i == len(arr)-1:
                print(arr[i])
            else:
                print(arr[i],end='')