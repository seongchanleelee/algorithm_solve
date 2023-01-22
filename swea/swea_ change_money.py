t = int(input())
arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1,t+1):
    n = int(input())
    answer = [0] * len(arr)
    for i in range(len(arr)):
        while n >= arr[i]:
            n -= arr[i]
            answer[i] +=1
    print(f"#{tc}")
    print(*answer)