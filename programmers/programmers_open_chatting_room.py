def solution(record):
    answer = []
    uid = {}
    Record = []
    for i in record:
        Record.append(list(i.split()))

    for rec in Record:
        if rec[0] == "Enter":
            if rec[1] not in uid:
                uid[rec[1]] = rec[2]
            else:
                uid[rec[1]] = rec[2]

        elif rec[0] == 'Leave':
            if rec[1] not in uid:
                uid[rec[1]] = rec[2]

        else:# Change
            if rec[1] in uid:
                uid[rec[1]] = rec[2]

    for i in range(len(Record)):
        if Record[i][0] =="Enter":
            answer.append(f"{uid[Record[i][1]]}님이 들어왔습니다.")

        elif Record[i][0] == "Leave":
            answer.append(f"{uid[Record[i][1]]}님이 나갔습니다.")
    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))