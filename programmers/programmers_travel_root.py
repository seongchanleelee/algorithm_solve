import copy
def solution(tickets):
    # 'ICN'으로 시작하는 티켓들중, 알파벳 순서대로 시작하게 끔 SORT
    tickets.sort(key=lambda x: (x[0]=='ICN',-ord(x[1][0])),reverse=True)

    # tickets1 = []
    # tickets2 = []
    # for i in range(len(tickets)):
    #     if tickets[i][0] =='ICN':
    #         tickets1.append(tickets[i][1])
    #     else:
    #         tickets2.append(tickets[i][1])

    len_ticket = len(tickets)
    answer = []
    visit=[0]*len(tickets)
    lst = []

    def dfs(level, st):
        nonlocal lst, answer
        answer.append(st)
        if level ==len_ticket-1:
            lst.append(answer)
            answer = []
            return

        for i in range(len(tickets)):
            if tickets[i][0] !=st: continue
            if visit[i] ==1: continue
            # if tickets[i][0] =='ICN':
            #     if (tickets[i][1] in tickets1) and (tickets[i][1] in tickets2):
            #         continue
            visit[i] = 1
            dfs(level+1,tickets[i][1])
            visit[i] = 0

    dfs(0,'ICN')

    return lst
# print(solution([["ICN", "SFO"],["ICN","AAA"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# print(solution([["ICN", "A"], ["ICN", "A"], ["ICN", "A"], ["A", "ICN"], ["A", "ICN"]]))

print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))