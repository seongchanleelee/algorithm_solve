import copy
# t = int(input())
# for tc in range(t):
#     n = int(input())
#     arr = []
#     lenArr=[0]*11
#     for i in range(n):
#         arr.append((input()))
#     result = True
#
#     arr.sort(key=lambda x: (len(x), x))
#
#     for i in range(len(arr)):
#         lenArr[len(arr[i])]+=1
#
#     st = 0
#     for i in range(len(lenArr)):
#         if st >= len(arr):
#             break
#
#         if result ==False:
#             break
#
#         if lenArr[i] != 0:
#             while lenArr[i] !=0:
#                 if result ==False:
#                     break
#                 lenArr[i] -=1
#
#                 for j in range(st+1,len(arr)):
#                     if arr[st] == arr[j][:i]:
#                         result = False
#                         break
#                 st+=1
#     if result ==False:
#         print('NO')
#     else:
#         print('YES')

#####################tri 개념###############################
t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input().strip())
    arr.sort()

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1][0:len(arr[i])]:
            print('NO')
            break
    else:
        print('YES')

