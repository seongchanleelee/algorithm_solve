n = int(input())
arr = []
for i in range(n):
    arr.append(input())

Max = len(arr[0])

for i in range(len(arr)):
    if Max !=len(arr[i]):
        arr[i] += '='*(Max-len(arr[i]))

answer = ''
for i in range(Max):
    lst = []
    for j in range(n):
        lst.append(arr[j][i])
    if len(set(lst)) == 1:
        answer += lst[0]
    else:
        answer += '?'
print(answer)
