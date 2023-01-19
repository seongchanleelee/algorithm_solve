t = int(input())
for tc in range(1,t+1):
    yn = 1
    s = input()
    b = s[::-1]
    if s ==b:
        yn = 1
    else:
        yn = 0
    print(f"#{tc} {yn}")