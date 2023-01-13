
def solution(n, words):
    answer = [words[0]]
    arr = [1] + [0] * (n-1)
    for i in range(1,len(words)):
        if words[i-1][-1:] == words[i][0]:
            if words[i] not in answer:
                # print(i % n +1)
                arr[(i % n)] += 1
                answer.append(words[i])

            else:
                return [(i%n)+1, arr[i%n]+1]
        else:
            return [(i%n)+1, arr[i%n]+1]

    return [0,0]
print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))