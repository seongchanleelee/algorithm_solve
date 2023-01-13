t = int(input())
for tc in range(t):
    n = int(input())
    if n >= 4:
        arr = [0]*(n+1)
        arr[1] = 1
        arr[2] = 2
        arr[3] = 4
    else:
        arr = [0,1,2,4]

    if n>=4:
        for i in range(4, n+1):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    print(arr[n])