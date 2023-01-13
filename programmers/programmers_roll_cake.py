def solution(topping):
    answer = 0
    end = len(topping)
    for i in range(len(topping)):
        left=set(topping[0:i])
        right = set(topping[i:end])
        print(left, right)
        if len(left) == len(right):
            answer +=1

    print(answer)
    return answer
# solution([1, 2, 1, 3, 1, 4, 1, 2])
# solution([1, 2, 3, 1, 4])

# def solution(topping):
#     answer = 0
#     start = 0
#     # mid = len(topping)//2
#     end = len(topping)
#     while start < end:
#         mid = (start+end)//2
#         left = topping[0:mid]
#         right = topping[mid: len(topping)]
#         # 토핑갯수
#         if len(set(left)) == len(set(right)):
#             answer +=1
#             if len(left) > len(right):
#                 start +=1
#             elif len(left) <= len(right):
#                 end -=1
#         else:
#             if len(left) > len(right):
#                 start +=1
#             elif len(left) <= len(right):
#                 end -=1
#
#     print(answer)
#     return answer

from collections import Counter


# def solution(topping):
#     dic = Counter(topping)
#     set_dic = set()
#     answer = 0
#     for i in topping:
#         dic[i] -= 1
#         set_dic.add(i)
#         if dic[i] == 0:
#             dic.pop(i)
#         if len(dic) == len(set_dic):
#             answer += 1
#
#     return answer

def solution(topping):
    answer = 0
    dic = dict()
    print(dic)
    for i in range(len(topping)):
        if topping[i] not in dic:
            dic[topping[i]] = 1
        else:
            dic[topping[i]] +=1

    set_dic = set()
    for i in range(len(topping)):
        dic[topping[i]] -=1
        set_dic.add(topping[i])
        if dic[topping[i]] ==0:
            dic.pop(topping[i])
        if len(dic) == len(set_dic):
            answer +=1
    print(answer)
    return answer

solution([1, 2, 1, 3, 1, 4, 1, 2])
solution([1, 2, 3, 1, 4])