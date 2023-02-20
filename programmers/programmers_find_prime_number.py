import itertools
def solution(numbers):
    result=[]
    for i in range(1,len(numbers)+1):
        a=list(map(''.join,itertools.permutations(numbers,i)))
        for j in list(set(a)):
            if int(j)<=1: # 0혹은 1일경우를 고려하여 제거.
                continue
            con=True
            for c in range(2,int(int(j)**0.5)+1):
                if int(j)%c==0:
                    con=False  #소수가 아닐 경우 con=False
                    break
            if con:
                result.append(int(j))
    return len(set(result))
solution("17")
solution("011")