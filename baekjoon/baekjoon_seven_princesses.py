arr = [input() for i in range(5)]

prin = [[0 for i in range(5)] for j in range(5)]

diry = [1, -1, 0, 0]
dirx = [0, 0, 1, -1]

visit = [[0 for i in range(5)] for j in range(5)]
ans = 0
p = []


def check(s):
    global visit
    y = s // 5
    x = s % 5

    for i in range(4):
        ty = y + diry[i]
        tx = x + dirx[i]

        if ty >= 0 and ty < 5 and tx >= 0 and tx < 5:
            if visit[ty][tx] == 0:
                if (ty * 5 + tx) in p:
                    visit[ty][tx] = 1
                    check((ty * 5 + tx))


def dfs(cnt, idx, yn):
    global ans
    global visit

    if yn >= 4 or 25 - idx < 7 - cnt:
        return

    if cnt == 7:

        check(p[0])
        if sum(sum(visit, [])) == 7:
            ans += 1
        visit = [[0 for i in range(5)] for j in range(5)]
        return

    y = idx // 5
    x = idx % 5

    p.append(idx)
    if arr[y][x] == 'Y':
        dfs(cnt + 1, idx + 1, yn + 1)
    else:
        dfs(cnt + 1, idx + 1, yn)

    p.pop()
    dfs(cnt, idx + 1, yn)


dfs(0, 0, 0)
print(ans)
##############################################################
# from collections import deque
# import copy
# lst = [list(input()) for _ in range(5)]
# arr = []
# for y in range(5):
#     for x in range(5):
#         arr.append(lst[y][x])
#
# visit = [0]*25
# path = ['']*7
# result = 0
# yx = []
# def index(idx):
#     used = [[0] * 5 for _ in range(5)]
#     yx = []
#     for i in range(len(idx)):
#         Y = idx[i]//5
#         X = idx[i]%5
#         yx.append((Y,X))
#
#     while yx:
#         directy = [-1, 1, 0, 0]
#         directx = [0, 0, -1, 1]
#         q = deque()
#         q.append(yx[0])
#
#         nowy,nowx = q.popleft()
#         for i in range(4):
#             dy = directy[i] + nowy
#             dx = directx[i] + nowx
#
#             if 0<=dy<5 and 0<=dx<5:
#                 if used[dy][dx] ==1: continue
#                 if (dy*5+dx) in idx:
#                     used[dy][dx] = 1
#                     yx.pop(0)
#
# def dfs(level,y,idx):
#     global result
#     if y >=4:
#         return
#
#     if level ==7:
#         cnt = 0
#         for i in range(len(path)):
#             #################################3
#             if path[i] =='Y':
#                 cnt+=1
#             if cnt >=4:
#                 return
#             else:
#                 # 인접인지 아닌지 확인
#                 index(idx)   #[0,1,2,3,4,5,6]
#
#         return
#
#     for i in range(len(arr)): #25
#         if visit[i] ==1: continue
#         visit[i] = 1
#         path[level] = arr[i]
#         if arr[i] =='Y':
#             dfs(level+1,y+1,idx+[i])
#             visit[i] = 0
#         else:
#             dfs(level+1,y,idx+[i])
#             visit[i] = 0
#
# dfs(0,0,[])