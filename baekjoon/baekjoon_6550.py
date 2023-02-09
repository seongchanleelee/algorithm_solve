while 1:
    try:
        s,t = list(input().split())

        s = list(s)
        t = list(t)

        for i in t:
            if s == []:
                break
            if i == s[0]:
                s.pop(0)

        if s == []:
            print('Yes')
        else:
            print('No')
    except:
        break
