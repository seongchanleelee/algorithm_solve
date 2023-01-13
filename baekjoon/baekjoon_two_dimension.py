from collections import Counter
import copy
r,c,k = list(map(int,input().split()))
for i in range(3):
    arr=[list(map(int, input().split())) for _ in range(3)]

    cnt = 0
    while arr[r-1][c-1] !=k:
    # while 1:
        if len(arr) >=100:
            for y in range(len(arr)):
                arr = arr[0:101]
        if len(arr[0]) >=100:
            for y in range(len(arr)):
                arr[y] = arr[y][0:101]

        cnt += 1
        if cnt ==100:
            print(-1)
            break


        if len(arr) >= len(arr[0]):   #행의수 >= 열의수
            result = []
            for y in range(len(arr)):
                dic = Counter(arr[y])
                dic= sorted(dic.items())
                dic = sorted(dic, key = lambda x: x[1])

                if dic[0][0] ==0:
                    dic.pop(0)

                # 이차원 배열을 만들어 재배치해줌
                arr2 = []
                for y in range(len(dic)):
                    arr2.append(dic[y][0])
                    arr2.append(dic[y][1])
                result.append(arr2)

            # 최대길이 구하기
            Max = 0
            for i in range(len(result)):
                Max = max(len(result[i]), Max)

            # 최대 길이만큼 0 넣어주기
            for i in range(len(result)):
                result[i] +=[0]*(Max - len(result[i]))
            arr = result

        else:
            # 열을 기준으로 배열 뽑기
            result = []
            for y in range(len(arr[0])):
                dic = dict()
                arr2 = []
                for x in range(len(arr)):
                    if arr[x][y] !=0:
                        if arr[x][y] in dic:

                            dic[arr[x][y]] += 1
                        else:
                            dic[arr[x][y]] = 1
                dic = sorted(dic.items())
                dic = sorted(dic, key=lambda x: x[1])
                # 2차원 배열 만들어줌
                arr2 = []
                for y in range(len(dic)):
                    arr2.append(dic[y][0])
                    arr2.append(dic[y][1])
                result.append(arr2)
                print(result)

            # max값확인
            Max = 0
            for y in range(len(result)):
                Max = max(len(result[y]), Max)

            # 0집어넣기
            for y in range(len(result)):
                result[y] +=[0]*(Max - len(result[y]))

            # 열로 뒤집기
            result_copy = copy.deepcopy(result)
            result = list(map(list, zip(*result)))
            print(result)
            # result = [[0]*len(result_copy) for _ in range(len(result_copy[0]))]
            # for y in range(len(result)):
            #     for x in range(len(result[y])):
            #         result[x][y] = result_copy[y][x]
            # print(result)
            arr = result

    print(cnt)


#
# from collections import Counter
#
#
# def r_operation(arr):  # R 연산
#     for i in range(len(arr)):
#         temp = []
#         for j in range(len(arr[i])):
#             if arr[i][j] != 0:
#                 temp.append(arr[i][j])
#
#         counter = Counter(temp)
#         temp = []
#         for key in counter.keys():
#             temp.append((key, counter[key]))
#         temp = sorted(temp, key=lambda x: (x[1], x[0]))
#         for j in range(50):
#             if j < len(temp):
#                 arr[i][j * 2] = temp[j][0]
#                 arr[i][j * 2 + 1] = temp[j][1]
#             else:
#                 arr[i][j * 2] = 0
#                 arr[i][j * 2 + 1] = 0
#     return arr
#
#
# def c_operation(arr):  # C 연산
#     for i in range(len(arr)):
#         temp = []
#         for j in range(len(arr)):
#             if arr[j][i] != 0:
#                 temp.append(arr[j][i])
#
#         counter = Counter(temp)
#         sort_arr = []
#         for key in counter.keys():
#             sort_arr.append((key, counter[key]))
#
#         sort_arr = sorted(sort_arr, key=lambda x: (x[1], x[0]))
#         for j in range(50):
#             if j < len(sort_arr):
#                 arr[j * 2][i] = sort_arr[j][0]
#                 arr[j * 2 + 1][i] = sort_arr[j][1]
#             else:
#                 arr[j * 2][i] = 0
#                 arr[j * 2 + 1][i] = 0
#     return arr
#
#
# def find_col_index(arr):
#     index = 0
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i][j] == 0:
#                 index = max(index, j)
#                 break
#     return index
#
#
# def find_row_index(arr):
#     index = 0
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[j][i] == 0:
#                 index = max(index, j)
#                 break
#     return index
#
#
# if __name__ == "__main__":
#     R, C, K = map(int, input().split())
#     array = [[0] * 101 for _ in range(101)]
#     for i in range(3):
#         a, b, c = map(int, input().split())
#         array[i][0], array[i][1], array[i][2] = a, b, c
#
#     flag = True
#     for i in range(0, 101):
#         if array[R - 1][C - 1] == K:
#             print(i)
#             flag = False
#             break
#         if find_row_index(array) >= find_col_index(array):
#             array = r_operation(array)
#         else:
#             array = c_operation(array)
#
#     if flag:
#         print(-1)