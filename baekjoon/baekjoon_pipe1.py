# n = int(input())
# arr = [list(map(int,input().split()))for _ in range(n)]
# dp =[[0]*n for _ in range(n)]
# print(arr)
# print(dp)
# directy = [0,1,1] # 우 우하 하
# directx = [1,1,0]
# now = [0,0]
# num = []
# for y in range(n):
#     for x in range(1, n):
#         num = [y -  now[0] , x - now[1]]
#         if num ==[0,1]: #시작이 가로인경우
#             now = [y,x]
#             if 0<=y + directy[0]< n and 0<=x + directx[0]<n:
#                 if arr[y + directy[0]][x + directx[0]] !=1:
#                     dp[y + directy[0]][x + directx[0]] +=1
#             if 0 <= y + directy[1] <n and x + directx[1]<n:
#                 if arr[y + directy[1]][x + directx[1]] !=1:
#                     dp[y + directy[1]][x + directx[1]] +=1
#             pass
#
#         elif num == [1,0]: #시작이 세로인경우
#             now = [y,x]
#             if 0 <= y + directy[2] < n and 0 <= x + directx[2]<n:
#                 if arr[y + directy[2]][x + directx[2]] !=1:
#                     dp[y + directy[2]][x + directx[2]] +=1
#             if 0 <= y + directy[1] < n and 0 <= x + directx[1]<n:
#                 if arr[y + directy[1]][x + directx[1]] != 1:
#                     dp[y + directy[1]][x + directx[1]] +=1
#             pass
#
#         elif num ==[1,1]: #시작이 대각인경우
#             now = [y,x]
#             if 0 <= y + directy[0] < n and 0 <= x + directx[0]<n:
#                 if arr[y + directy[0]][x + directx[0]] !=1:
#                     dp[y + directy[0]][x + directx[0]]+=1
#             if 0 <= y + directy[1] < n and 0 <= x + directx[1]<n:
#                 if arr[y + directy[1]][x + directx[1]] !=1:
#                     dp[y + directy[1]][x + directx[1]]+=1
#             if 0 <= y + directy[2] < n and 0 <= x + directx[2]<n:
#                 if arr[y + directy[2]][x + directx[2]] != 1:
#                     dp[y + directx[2]][x + directx[2]]+=1
#             pass
#
# print(dp)


# 0 → ─, 1 → /, 2 → |

def solution():
    # 1행 미리 처리하기 → (3) 과정
    dp[0][0][1] = 1
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]

    # 왜 1행과 1열을 제외하는지는 (3), (4) 과정에서 봤었죠?
    for r in range(1, N):
        for c in range(1, N):
            # (5) 과정
            # 대각선 파이프를 추가하는 과정
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

            # 가로, 세로 파이프를 추가하는 과정
            if board[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

    print(dp)
    # 최종 결과 출력
    print(sum(dp[i][N - 1][N - 1] for i in range(3)))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
solution()

