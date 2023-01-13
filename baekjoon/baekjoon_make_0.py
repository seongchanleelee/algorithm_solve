t = int(input())
lst = [' ','+','-']
cnt = 0
for tc in range(t):
    n = int(input())
    path = []
    result = []
    for i in range(1,n+1):
        path.append(i)
        path.append('')
    path.pop(-1) ## [1,'',2,'',3]
    arr = []
    used = [0]*3
    # # tc마다 줄바꿈을 해주기 위한 cnt
    # if cnt >=1:
    #     print()
    # cnt=1
    def dfs(level):
        global Sum, arr, result
        if level==2*n-1:

            for i in range(len(path)):
                arr.append(path[i])

            while ' ' in arr:
                a = arr.index(' ')
                arr[a] = int(str(arr[a-1])+str(arr[a+1]))    ##[12,+3+4-5, ,6]  ==> 12+3+4-56
                arr.pop(a-1)
                arr.pop(a)

            Sum = arr[0]
            for i in range(1,len(arr),2):
                if arr[i] =='+':
                    Sum += arr[i+1]
                if arr[i] =='-':
                    Sum -= arr[i+1]
            if Sum == 0:
                for i in range(len(path)):
                    print(path[i],end='')
                print()
            arr= []
            return

        for i in range(3):
            path[level] = lst[i]
            dfs(level+2)
    dfs(1)
######################################################
# def dfs(level):
#     global path
#
#     if level == n+1:
#         sumV = 1       # 2부터 계산할 것이므로
#         for i in range(len(path)):   # 1은 계산할 필요가 없다.
#             if i == 0:
#                 continue
#             if i % 2 == 1:      # 연산자는 넘어간다 -> 숫자만 확인
#                 continue
#             # if i+1 < len(path):     # index error 발생 방지
#             #     if path[i+1] == ' ':
#             #         continue
#             if path[i-1] == '+':    # 본격 연산
#                 sumV += path[i]
#             elif path[i-1] == '-':
#                 sumV -= path[i]
#             elif path[i-1] == ' ':
#                 if path[i-3] == '-':
#                     sumV += int('-' + str(path[i-2])+str(path[i]))
#                 else:
#                     sumV += int(str(path[i - 2]) + str(path[i]))
#                     if i == 2:
#                         sumV -= 1
#
#         if sumV == 0:
#             print(*path, sep='')
#         return
#
#     for i in range(3):      # +, -, 공백 순서
#         if i == 0:      # + 인 경우
#             path.append(' ')
#         elif i == 1:    # - 인 경우
#             path.append('+')
#         elif i == 2:    # 공백인 경우
#             path.append('-')
#         path.append(level)
#         dfs(level+1)
#         path.pop()      # level 빼기
#         path.pop()      # 연산자 빼기
#
# N = int(input())
# for i in range(N):
#     n = int(input())
#     path = [1]
#     dfs(2)