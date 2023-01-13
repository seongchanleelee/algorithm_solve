# t = int(input())
# for tc in range(t):
#     group = [0]*100000
#     arr = []
#     n = int(input())
#     for nc in range(1,n+1):
#         x,y = input().split()
#         if x not in arr:
#             arr.append(x)
#         if y not in arr:
#             arr.append(y)
#
#         if group[arr.index(x)] ==0:
#             group[arr.index(x)] =nc
#         else:
#             a=group[arr.index(x)]
#             for i in range(len(group)):
#                 if group[i] != 0 and group[i] ==a:
#                     group[i] = nc
#
#
#         if group[arr.index(y)] ==0:
#             group[arr.index(y)] = nc
#         else:
#             a=group[arr.index(y)]
#             for i in range(len(group)):
#                 if group[i] !=0 and group[i] == a :
#                     group[i] = nc
#
#         cnt = 0
#         for i in range(len(group)):
#             if group[i] == nc:
#                 cnt +=1
#         print(cnt)
########################################################
def find(a):
    if a ==group[a]:
        return a
    else:
        a_boss = find(group[a])
        group[a] = a_boss
        return group[a]

def union(x,y):
    x_boss = find(x)
    y_boss = find(y)

    if x_boss != y_boss:
        group[y_boss] = x_boss
        number[x_boss] += number[y_boss]

t = int(input())
for tc in range(t):
    group = dict()
    number = dict()

    n = int(input())
    for _ in range(n):
        x,y = input().split()

        if x not in group:
            group[x] = x
            number[x] = 1
        if y not in group:
            group[y] = y
            number[y] = 1
        union(x,y)
        print(number[find(x)])