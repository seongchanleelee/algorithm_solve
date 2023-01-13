from itertools import permutations
def solution(numbers):
    numbers = list(numbers)
    path = []
    used = [0] * len(numbers)
    answer = 0
    # 썻던 숫자배열은 사용못하게 함
    visit =[]
    def dfs(level):
        nonlocal answer
        # 문자열 수를 합성시켜줌
        num = '0'
        for i in range(len(path)):
            num += (path[i])

        a=int(num)
        #사용했던 숫자배열인지 확인
        cnt = 0
        if a not in visit:
            visit.append(a)

            # 소수인지 확인
            for i in range(2, int(num) + 1):
                if int(num) / i == int(int(num) / i):
                    cnt += 1

                    if cnt >=2:
                        break

        # 나누어지는 수가 1과 본인만 있을시(소수일시)
            if cnt == 1:
                answer += 1

        else:
            return

        # 재귀를 통해 숫자조합을 만들어줌
        for i in range(len(numbers)):
            if used[i] == 1: continue
            used[i] = 1
            path.append(numbers[i])
            dfs(level + 1)
            path.pop(level)
            used[i] = 0

    dfs(0)

    return answer
print(solution("1234567"))

#------------------------
def solution(numbers):
    case = []
    for i in range(1,len(numbers)+1):
        tmp = permutations(numbers,i)

        for n in tmp:
            tmp_str = ''.join(n)
            case.append(int(tmp_str))

    case = list(set(case))
    return dfs(case)


def dfs(case):
    prime_count = 0
    for n in case:
        count =0
        for i in range(2,n):
            if n % 1 ==0: count +=1


        if n >1 and count ==0:
            prime_count +=1
    return prime_count
