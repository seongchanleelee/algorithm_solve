def solution(n,computers):
    answer = 0
    visit = [0] * n

    def dfs(now):
        visit[now] = 1
        for i in range(n):
            if computers[now][i]==1 and visit[i]!=1:
                dfs(i)

    for i in range(n):
        if visit[i] !=1:
            dfs(i)
            answer+=1
    return answer
