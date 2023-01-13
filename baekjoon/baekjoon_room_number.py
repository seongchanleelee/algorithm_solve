n = int(input())
p = list(map(int,input().split()))
m = int(input())
result = []

# st = n-1
# cnt = 0
# # cnt2 = n
# while m != 0:
#     if st == -1:
#         cnt +=1
#         st = n-1 -cnt
#         # if st ==-1:
#         #     break
#         m = m+p[st+1]
#         result.pop()
#
#
#     for i in range(st,-1,-1):
#         result.append(i)
#         if m-p[i] >=0:
#             m=m-p[i]
#             # result.append(i)
#             # st = n-1
#             break
#
#         else:
#             result.pop()
#             st-=1
#             break
#
# for i in range(len(result)):
#     print(result[i],end='')

while m !=0:

    for i in range(1,len(p)):
        if m - p[i] >0:
            m = m - p[i]
            result.append(i)

            for i in range(len(p)):
                if m - p[i] >0:
                    m = m - p[i]

