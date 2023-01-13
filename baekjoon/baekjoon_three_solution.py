# n = int(input())
# arr = list(map(int,input().split()))
# path = ['']*3
# used=[0]*n
# Min = 21e8
# result = []
# def dfs(level):
#     global Min, result
#
#     if level ==3:
#         if Min > abs(path[0]+path[1]+path[2]):
#             Min = abs(path[0] + path[1] + path[2])
#             result = [path[0],path[1],path[2]]
#         return
#
#     for i in range(n):
#         if used[i] ==1: continue
#         used[i] =1
#         path[level] = arr[i]
#         dfs(level+1)
#         used[i] = 0
# dfs(0)
# result.sort()
# print(*result)

#-------------------------투포인터를 이용--------------
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
Min = 21e8
result = []
for i in range(n-2):
    a3 = arr.pop()

    st = 0
    ed = len(arr)-1
    while st!= ed:
        Sum = a3 + arr[ed] + arr[st]
        if Min > abs(Sum):
            Min = abs(Sum)
            result = [a3,arr[st], arr[ed]]
        if Sum < Min:
            st +=1
        else:
            ed -=1

        if Min ==0:
            result = [a3,arr[ed], arr[st]]
            break
    if Min ==0:
        break
print(*sorted(result))









