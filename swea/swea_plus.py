t = int(input())
for tc in range(1,t+1):
    arr = list(map(int,input().split()))

    #시 계산
    hour = arr[0] + arr[2]
    if hour >12:
        hour = hour - 12
    minute = arr[1] + arr[3]
    if minute >60:
        minute = minute - 60
        hour +=1
    print(f"#{tc} {hour} {minute}")