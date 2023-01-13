import sys
input = sys.stdin.readline

n = int(input())
# 3가지 경우가 있음. 아무것도 두지않거나, 왼쪽에 두거나, 오른쪽에 두거나
arr = [[0]*3 for _ in range(n + 1)]
arr[1][0], arr[1][1], arr[1][2] = 1, 1, 1

# 0은 아무것도 두지 않을때, 1은 왼쪽에 두었을때, 2는 오른쪽에 두었을때
for i in range(2, n+1):
    arr[i][0] = (arr[i-1][0] + arr[i-1][1] + arr[i-1][2]) % 9901
    arr[i][1] = (arr[i-1][0] + arr[i-1][2]) % 9901
    arr[i][2] = (arr[i-1][0] + arr[i-1][1]) % 9901

print(sum(arr[n]) % 9901)