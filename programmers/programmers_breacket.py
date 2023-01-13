def solution(s):
    answer = 0
    s = list(s)

    for i in range(len(s)):
        for j in range(len(s)-1):
            s[j], s[j+1] =s[j+1], s[j]
        stack = []
        for k in range(len(s)):
            if stack ==[]:
                stack.append(s[k])
                continue
            elif stack[-1] =="[":
                if s[k] == "]":
                    stack.pop(-1)
                    continue
            elif stack[-1] =="{":
                if s[k] == "}":
                    stack.pop(-1)
                    continue
            elif stack[-1] =="(":
                if s[k] ==")":
                    stack.pop(-1)
                    continue
            stack.append(s[k])
        if len(stack) ==0:
            answer+=1
    print(answer)
    return answer
solution("[](){}")
solution("}]()[{")
solution("[)(]")
solution("}}}")
