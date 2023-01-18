t = int(input())
for tc in range(1,t+1):
    s = input()
    answer = 0
    for i in range(1, 11):
        if s[:i] != s[i:i+i]:
            continue
        else:
            answer = i
            break
    print(f"#{tc} {answer}")

