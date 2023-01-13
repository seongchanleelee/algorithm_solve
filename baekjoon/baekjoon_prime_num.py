m = int(input())
n = int(input())
arr = []
for i in range(m,n+1):
    set = False
    if i != 1:
        for j in range(2,i):
            if i%j ==0:
                set = True
                break
            else:
                set = False
        if set == False:
            arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
