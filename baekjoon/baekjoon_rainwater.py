h, w = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(1, w-1):
    leftmax = max(arr[:i])
    rightmax = max(arr[i+1:])

    fin = min(leftmax, rightmax)

    if arr[i] < fin:
        result += fin - arr[i]
print(result)