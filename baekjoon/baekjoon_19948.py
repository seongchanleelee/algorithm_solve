# 97 ~ 122 a ~ z
# aaaaaaaaaaaaaaaaaaa는 a -=1인거를 적용시켜주기
s = list(input())
space = int(input())
alpha = list(map(int,input().split()))

isDo = True
for i in range(len(s)):
    if s[i] !=' ':
        if s[i].islower() == False:
            s[i]=s[i].lower()


    if 97<=ord(s[i])<=122:
        # if i !=0:
        #     if s[i] == s[i-1]: continue

        if alpha[ord(s[i])-97] >0:
            alpha[ord(s[i])-97] -=1
        elif alpha[ord(s[i])-97] <=0:
            # 키보드 횟수 넘어가면 부수기
            isDo = False
            break
    if s[i] ==' ' and s[i-1] !=' ':
        space -=1
        # alpha[ord(s[i-1])-97] -=1
    if space <0:
        isDo = False
        break

title = ''
if isDo == True:
    title+=s[0]
    for i in range(len(s)):
        if s[i-1] ==' ' and s[i] != ' ':
            title+=s[i]
print(title)
print(alpha)
result = ''
if title != '':
    for i in range(len(title)):
        if 97 <= ord(title[i]) <= 122:
            # if i != 0:
            #     if title[i] == title[i - 1]: continue
            if alpha[ord(title[i]) - 97] > 0:
                alpha[ord(title[i]) - 97] -= 1
                result+=title[i].upper()
            elif alpha[ord(title[i]) - 97] <= 0:
                result = -1
                break
else:
    result = -1
print(alpha)
print(result)