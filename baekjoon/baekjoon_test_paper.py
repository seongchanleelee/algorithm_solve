# n,k = list(map(int,input().split()))
# arr = list(map(int,input().split()))
# group = []
# st =0
# while st != n:
#     lst = []
#     for i in range(st,st+(n//k)):
#         lst.append(arr[i])
#     st =i+1
#     group.append(lst)
#
# Min = 21e8
# group.sort(key=lambda x: sum(x))
# print(sum(group[0]))
################################################
n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))

st = 0
ed = sum(arr)+1

while st+1 <ed:
    mid = (st+ed)//2
    kcnt = 0
    temp = 0
    for i in range(n):
        temp+=arr[i]
        if temp >= mid:
            kcnt +=1
            temp = 0
    if kcnt >=k:
        st = mid
    else:
        ed = mid
print(st)