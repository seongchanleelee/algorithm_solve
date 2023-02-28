# 단위 시간으로 떨어지지 않으면 금액을 올림 함
# 차량 번호가 작은 자동차부터 청구
#fees[0]: 기본 시간(분) fees[1]: 기본 요금(원) fees[2]: 단위시간(분) fees[3]: 단위 요금(원)
import math
def solution(fees, records):
    dic = {}
    for i in range(len(records)): #[0]: 시간 [1]: 차량번호 [2]: 입출차내용
        records[i] = list(records[i].split())

    for i in range(len(records)):
        if records[i][1] not in dic:
            dic[records[i][1]] = [records[i][0], records[i][2],0]

        else:
            if records[i][2] == 'OUT':
                # 시간 계산
                if int(records[i][0][3:5]) > int(dic[records[i][1]][0][3:5]):
                   dic[records[i][1]][2] += (int(records[i][0][0:2]) - int(dic[records[i][1]][0][0:2])) * 60 + (
                           int(records[i][0][3:5]) - int(dic[records[i][1]][0][3:5]))
                else:
                    dic[records[i][1]][2] += (int(records[i][0][0:2]) - int(dic[records[i][1]][0][0:2])-1) * 60 + (
                           abs(60 + int(records[i][0][3:5]) - int(dic[records[i][1]][0][3:5])))
                dic[records[i][1]][1] = 'OUT'
            else:
                dic[records[i][1]][1] = 'IN'
                dic[records[i][1]][0] = records[i][0]

    # 입차 후 출차를 하지 않은 차량 시간 계산
    for d in dic:
        if dic[d][1] =='IN':
            dic[d][2] += 59 - int(dic[d][0][3:5]) + (23 - int(dic[d][0][0:2]))*60

    # 차량번호순으로 정렬
    # dictionary 형태로 바꿔주지 않으면 튜플형태가 됨
    dic = dict(sorted(dic.items()))

    # 주차비 계산
    answer = []
    for d in dic:
        if dic[d][2] > fees[0]:
            answer.append(fees[1] + math.ceil(math.ceil(dic[d][2] - fees[0]) / fees[2]) * fees[3])
        else:
            answer.append(fees[1])

    return answer
