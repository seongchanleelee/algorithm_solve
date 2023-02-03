t = int(input())
for tc in range(1,t+1):
    n = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while n !=1:
        if n %11 ==0:
            n = n//11
            e +=1
        if n % 7 ==0:
            n = n//7
            d +=1
        if n % 5 ==0:
            n = n//5
            c +=1
        if n % 3 ==0:
            n = n//3
            b +=1
        if n % 2 ==0:
            n = n//2
            a +=1
    print(f"#{tc} {a} {b} {c} {d} {e}")