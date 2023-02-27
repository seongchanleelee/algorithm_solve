def solution(k, dungeons):
    used = [0]*len(dungeons)
    Max = 0
    def dfs(level, fatigue,ans):
        nonlocal Max
        if fatigue < 0:
            return

        if level ==len(dungeons):
            Max = max(Max, ans)
            return

        for i in range(len(dungeons)):
            if used[i] ==1: continue
            used[i] = 1
            if fatigue < dungeons[i][0]:
                dfs(level+1, fatigue,ans)
                used[i] = 0
            else:
                dfs(level+1, fatigue-dungeons[i][1], ans+1)
                used[i] = 0

    dfs(0,k,0)
    return Max

print(solution(80, [[80,20],[50,40],[30,10]]))