def solution(want, number, discount):
    answer = 0
    n = sum(number)
    for i in range(len(discount) - n+1):
        a = discount[i:i+n:1]
        require = [0] * len(number)
        for j in range(len(a)):
            if a[j] in want:
                if a[j] in want:
                    require[want.index(a[j])] +=1
        if require == number:
            answer +=1
    return answer

print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))
print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))