n =int(input())

arr = [0,0]
def dp(n):
    global arr
    if n == 0:
        return 0
    if n == 1:
        return 0
    # arr = [0,0]


    for i in range(2, n+1):
        a = i//2
        if i - (i//2) == i//2:
            b = i//2
        else:
            b = 1+(i//2)

        num = a * b
        arr.append(num)
    return
dp(n)
print(arr[-1]+ arr[-2])


