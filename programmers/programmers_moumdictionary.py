def dfs(start, level, word):
    global cnt
    global answer
    arr = ["A", "E", "I", "O", "U"]

    if start == word:
        answer = cnt
        return
    if level ==5:
        return
    for i in range(5):
        cnt +=1
        dfs(start + arr[i], level+1, word)

cnt = 0
answer = 0
def solution(word):
    global answer
    dfs("",0, word)
    return answer
