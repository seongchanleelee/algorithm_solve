n = int(input())
s = []
for i in range(n):
    s.append(input())
result = ''

st, ed = 0, n-1
while st <= ed:
    if s[st] < s[ed]:
        result += s[st]
        st +=1
    elif s[st] > s[ed]:
        result += s[ed]
        ed -=1
    # 투 포인터 에 투포인터
    else:
        ST, ED = st, ed
        tf = False
        while ST <= ED:
            if s[ST] < s[ED]:
                result +=s[st]
                st +=1
                tf = True
                break
            elif s[ST] > s[ED]:
                result += s[ed]
                ed -=1
                tf = True
                break
            else:
                ST +=1
                ED -=1
        if not tf:
            result += s[st]
            st +=1
    if len(result) >=80:
        print(result)
        result = ''
print(result)

