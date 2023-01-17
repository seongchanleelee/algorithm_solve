import sys
input = sys.stdin.readline
t = int(input())
type0 = [1,1,1,0,1,1,1]
type1 = [0,0,1,0,0,1,0]
type2 = [1,0,1,1,1,0,1]
type3 = [1,0,1,1,0,1,1]
type4 = [0,1,1,1,0,1,0]
type5 = [1,1,0,1,0,1,1]
type6 = [1,1,0,1,1,1,1]
type7 = [1,1,1,0,0,1,0]
type8 = [1,1,1,1,1,1,1]
type9 = [1,1,1,1,0,1,1]
emp =   [0,0,0,0,0,0,0]
segment = [type0] + [type1] + [type2] + [type3] + [type4] + [type5] + [type6] + [type7] + [type8] + [type9] + [emp]
for tc in range(t):
    a,b = list(map(str,input().split()))

    if len(a) <=5:
        a = [10]*(5-len(a))+list(a)
    if len(b) <=5:
        b = [10]*(5-len(b)) + list(b)
    cnt = 0
    for i in range(5):
        if segment[int(b[i])] != segment[int(a[i])]:
            for j in range(7):
                if segment[int(b[i])][j] != segment[int(a[i])][j]:
                    cnt+=1
    print(cnt)



