n = int(input())

kang = 0
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
for i in range(n):

    order = i+1
    tip = arr[i] - (order - 1)
    if tip >=0:
        kang += tip
print(kang)