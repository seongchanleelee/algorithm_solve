s = list(input())
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))
# print(s)
# print(arr)


result = []
def dfs(level,word):
    if level == len(s):
        if s == word:
            result.append(1)
            return
        else:
            result.append(0)
            return
    if 1 in result:
        return

    if level > len(s):
        return

    for i in range(n):
        dfs(level+len(arr[i]),word+arr[i])
dfs(0,[])
# print(result)
if 1 in result:
    print(1)
else:
    print(0)

#-----------------------------dp를 활용함!---------------------------------
s = list(input())
n = int(input())
arr = []
dp_arr = [0] * 101
for _ in range(n):
    arr.append(list(input()))
result = 0

def dp(idx):
    global result
    if idx == len(s):
        result = 1
        return
    if dp_arr[idx] ==1:
        return
    dp_arr[idx] = 1

    for i in range(len(arr)):
        if len(s[idx:])>=len(arr[i]):
            for j in range(len(arr[i])):
                if arr[i][j] != s[idx+j]:
                    break
            else:
                dp(idx+len(arr[i]))
    return

dp(0)
print(result)