def solution(files):
    answer = []
    head = []
    number = []
    tail = []
    a = [' ','.','-']
    for i in range(len(files)):
        hea = ''
        num = ''
        tai = []
        numst = False
        n = 0
        for j in range(len(files[i])):
            if n ==0:
                if files[i][j].isnumeric() == True:
                    num += files[i][j]

                    if files[i][j+1].isnumeric() == False:
                        n = j
                else:
                    hea += files[i][j]
            else:
                tai.append(files[i][j:len(files[i])])
                break
        head.append(hea)
        number.append(num)
        tail.append(''.join(tai))

    # print(head)
    # print(number)
    # print(tail)

    # number
    for i in range(len(number)):
        number[i] = int(number[i])
    for j in range(len(number) - 1):
        for k in range(j, len(number)):
            if number[j] > number[k]:
                number[k], number[j] = number[j], number[k]
                files[k], files[j] = files[j], files[k]
    print(files)
    # head
    for i in range(len(head)):
        head[i] = head[i].lower()
    for i in range(len(head)-1):
        for j in range(i,len(head)):
            if head[i] > head[j]:
                head[i], head[j] = head[j], head[i]
                files[i], files[j] = files[j], files[i]
    print(files)

    # # number
    # for i in range(len(number)):
    #     number[i] = int(number[i])
    # for j in range(len(number)-1):
    #     for k in range(j,len(number)):
    #         if number[j] > number[k]:
    #             number[k], number[j] = number[j], number[k]
    #             files[k], files[j] = files[j], files[k]
    # print(files)
    # print(head)
    print(number)
    # print(tail)




    return answer

# solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])