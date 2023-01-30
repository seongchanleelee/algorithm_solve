t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort()

    print(f"#{tc}",end=" ")
    for i in range(len(arr)):
        print(arr[i],end=' ')
    print()