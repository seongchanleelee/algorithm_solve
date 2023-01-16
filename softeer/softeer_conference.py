# n, m = list(map(int,input().split())) # n: 회의실 수, m: 예약된 회의의 수
# arr =[]
# for i in range(n):
#     arr.append(input())
# arr.sort()
# lst = []
# # [r,s,t] r:회의실 이름, s:회의 시작시간, t:회의 끝나는 시간
# for i in range(m):
#     lst.append(list(input().split()))
# lst.sort()
# # print(arr)
# # print(lst)
#
# booklist = {}
# dic = {}
# for i in range(n):
#     booklist[arr[i]] = [0]*19
#     dic[arr[i]] = []
# # print(booklist)
#
#
# for i in range(m):
#     for j in range(int(lst[i][1]), int(lst[i][2])+1):
#         booklist[lst[i][0]][j] +=1
# # print(booklist)
#
#
# for i in booklist:
#     cnt = 0
#     st = 0
#     ed = 0
#     for j in range(9,17):
#         # if j ==16:
#         #     # print(bool(booklist[i][j] ==1 and booklist[i][j+1]==0))
#         #     # print(bool(booklist[i][j] ==0 or (booklist[i][j] ==1 and booklist[i][j+1]==0)))
#         if (booklist[i][j] ==0 or (booklist[i][j] ==1 and booklist[i][j+1]==0)) and st ==0:
#             st = j
#         elif booklist[i][j] >=1 and st!=0:
#             ed = j
#             dic[i].append([st,ed])
#             st = 0
#         if j ==16 and st:
#             dic[i].append([st,18])
# # print(dic)
#
# for i in dic:
#     a = str(len(dic[i]))
#     print("Room"+" "+i +":")
#     if dic[i] ==[]:
#         a = 'Not'
#         print(a +" " +"available")
#     else:
#         print(a + " " + "available:")
#     if dic[i] != []:
#         # for j in dic[i]:
#         for j in range(len(dic[i])):
#
#             if dic[i][j][0] <10:
#                 dic[i][j][0] = "09"
#     if dic[i] != []:
#         for k in dic[i]:
#             print(str(k[0]) + "-" + str(k[1]))
#
#
#
#
#         # for k in i:
#         #     print(k)
#         #     # print(str(k[0]) + "-" +str(k[1]))
#     if i != arr[-1]:
#         print("-----")
#
#
import sys
from collections import defaultdict

n, m= map(int, input().split())

meeting_name = defaultdict()

# 9-10-11-12-13-14-15-16-17-18
meeting_res_list = [[0 for _ in range(9)] for _ in range(n)]

for i in range(n):
    room_name = input()
    meeting_name[room_name] = i

for _ in range(m):
    name, start, end = input().split()
    for i in range( int(start)-9, int(end)-9):
        meeting_res_list[meeting_name[name]][i] = -1

meeting_name_sorted = (sorted(meeting_name.keys()))
total_cnt = 0
for key in meeting_name_sorted:
    print(f"Room {key}:")
    cnt = 0
    arr = []
    m_key = meeting_name[key]
    times = ''
    flag = False
    for meet in range(9):
        if not flag and meeting_res_list[m_key][meet] == 0:
            flag = True
            if meet == 0:
                times += "09"
            else:
                times += str(meet+9)
            times += '-'
        elif flag and meeting_res_list[m_key][meet] == 0:
            continue
        elif flag and meeting_res_list[m_key][meet] == -1:
            times += str(meet+9)
            arr.append(times)
            times = ''
            flag = False
            cnt += 1
    if flag:
        times += "18"
        arr.append(times)
        cnt += 1
    if cnt == 0:
        print("Not available")
    else:
        print(f"{cnt} available:")
        for time in arr:
            print(time)
    total_cnt+=1
    if total_cnt < n:
        print("-----")

