# import sys
# input = sys.stdin.readline
# n,m = list(map(int,input().split()))
#
# a = []
# for i in range(n):
#     a.append(int(input()))
# b = sorted(a)
#
# for i in range(n):
#     d = int(input())
#     st = 0
#     ed = n-1
#     while st <= ed:
#         mid = (st + ed)//2
#         if b[mid] == d:
#             if mid > 0:
#                 if b[mid-1] < b[mid]:
#                     print(mid)
#                     break
#                 else:
#                     ed = mid -1
#
#             else:
#                 print(mid)
#                 break
#         elif b[mid] > d:
#             ed =mid -1
#         else:
#             st = mid +1
#     print(-1)
import sys
input = sys.stdin.readline
n, m =list(map(int,input().split()))
a = [int(input()) for _ in range(n)]
d = [int(input()) for _ in range(m)]
b = sorted(a)

def search(d):
    st = 0
    ed = n-1
    while st <= ed:
        mid = (st + ed) //2
        if b[mid] ==d:
            if mid >0:
                if b[mid -1] < b[mid]:
                    return mid
                else:
                    ed = mid -1
            else:
                return mid
        elif b[mid] > d:
            ed = mid - 1
        else:
            st = mid + 1
    return -1

for i in d:
    print(search(i))



