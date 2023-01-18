t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    for i in range(n):
        if i ==0:
            arr[i][0] =1
            continue
        for j in range(0,n):
            if 1<=j<n-1:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            elif j ==0:
                arr[i][j] = arr[i-1][j]
            elif j == n-1:
                arr[i][j] = arr[i-1][j-1]
    print(f"#{tc}")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != 0:
                print(arr[i][j], end=' ')
        print('')
