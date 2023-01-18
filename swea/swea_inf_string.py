t = int(input())
for tc in range(1,t+1):
    S,T = list(input().split())

    s = S * len(T)
    t = T * len(S)

    if s == t:
        print(f"#{tc} yes")
    else:
        print(f"#{tc} no")