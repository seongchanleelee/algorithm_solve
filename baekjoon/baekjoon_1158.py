n, k =map(int,input().split())
arr = [0]*(n)
for i in range(1,n+1):
    arr[i-1] = i

st = k-1
result = []
visit = [0]*(n+1)
while arr !=[]:
    if st >=len(arr):
        while st < len(arr):
            st -= len(arr)
    result.append(arr[st])
    visit[arr[st]]=1
    st +=k

    if st >=len(arr):
        st -= len(arr)

        for i in range(n+1):
            if visit[i] ==1:
                arr.remove(i)
        visit = [0]*(n+1)

print('<',end='')
for i in range(len(result)):
    if i == len(result) -1:
        print(result[i],end='')
    else:
        print(f'{result[i]},',end=' ')
print('>')