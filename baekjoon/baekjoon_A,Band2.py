import sys
s = input()
t = input()
answer = 0
def dfs(t):
    global answer
    if t ==s:
        print(1)
        sys.exit()
        return

    if len(t) ==0:
        return 0
    if t[-1] =="A":
        dfs(t[:-1])

    if t[0] =="B":
        t = t[1:]
        t = t[::-1]
        dfs(t)
dfs(t)
print(0)
#
# import sys
# S=list(input())
# T=list(input())
# def dfs(t): # 문자열 T 리스트를 입력받아
#     if t==S:
#         print(1)
#         sys.exit()
#     if len(t)==0:
#         return 0
#     if t[-1]=='A': # 마지막이 A이면
#         dfs(t[:-1]) # 제거해서 재귀
#     if t[0]=='B': # 처음이 B이면
#         dfs(t[1:][::-1]) # B제거하고, 뒤집어서 재귀
# dfs(T)
# print(0)

