n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
st = 0
ed = arr[-1]

while st+1 < ed:
    height = (st+ed)//2

    tree = 0
    for i in range(len(arr)):
        if (arr[i] - height) >=0:
            tree+= arr[i] - height
    if tree >= m :
        st = height

    if tree< m:
        ed = height

print(st)
