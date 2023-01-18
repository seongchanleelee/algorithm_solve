t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    answer = 0
    Max = arr[-1]
    for i in range(n-2,-1,-1):
        if arr[i] >= Max:
            Max = arr[i]
        else:
            answer += Max - arr[i]
    print(f"#{tc} {answer}")