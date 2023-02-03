t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if n > m:
        n,m = m,n

    if len(b) < len(a):
        b,a = a,b
    Max = -21e8
    c=int(abs(m-n))+1
    for i in range(c):
        result = 0
        for j in range(n):
            result +=b[i+j] * a[j]
        Max = max(Max, result)

    print(f"#{tc} {Max}")