def solution(begin, target, words):
    begin = list(begin)
    target = list(target)
    for i in range(len(words)):
        words[i] = list(words[i])

    def bfs(begin, answer):
        q = []
        q.append((begin, answer))

        while q:
            nowbegin, nowanswer = q.pop(0)

            if nowbegin == target:
                return nowanswer

            if target not in words:
                return 0

            for y in range(len(words)):
                cnt = 0
                for x in range(len(words[y])):
                    if nowbegin[x] != words[y][x]:
                        cnt += 1
                if cnt == 1:
                    q.append((words[y], nowanswer + 1))


    answer = bfs(begin,0)
    return answer
begin= 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))

