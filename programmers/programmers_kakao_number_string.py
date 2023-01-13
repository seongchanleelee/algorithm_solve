def solution(s):
    answer = 0
    s=list(s)
    num = ['zero','one','two','three','four','five','six','seven','eight','nine']
    arr = [] # 문자인 경우 하나씩 받아줌
    lst = [] # 최종 결과값을 넣는 곳
    for i in range(len(s)):
        if ord('a')<=ord(s[i])<=ord('z'):
           arr.append(s[i])
           string = ''.join(arr) #arr을 문자화 시켜 num 안에 있는지 확인 시켜줌
           if string in num:
               lst.append(str(num.index(string)))
               arr = []
        else:
           lst.append(s[i])
    answer = int(''.join(lst))
    return answer

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))