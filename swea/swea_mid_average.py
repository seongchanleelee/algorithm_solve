t = int(input())
for tc in range(1,t+1):
    arr = list(map(int,input().split()))

    Max = max(arr)
    Min = min(arr)

    arr.remove(Max)
    arr.remove(Min)
    print(f"#{tc} {round(sum(arr)/len(arr))}")