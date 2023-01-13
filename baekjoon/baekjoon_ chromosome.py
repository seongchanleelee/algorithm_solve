t = int(input())

for tc in range(t):
    arr = list(input())
    start = 0

    #1케이스
    if arr[0] in ["A","B","C","D","E","F"]:
        if arr[0] !="A":
            start = 1
    else:
        print("Good")
        continue
    #2케이스
    if arr[start] !="A":
        print("Good")
        continue

    for i in range(start,len(arr)):
        if arr[i] != "A":
            start = i
            break

    #3케이스
    if arr[start] !="F":
        print("Good")
        continue
    for i in range(start,len(arr)):
        if arr[i] != "F":
            start = i
            break

    #4케이스
    if arr[start] !="C":
        print("Good")
        continue
    for i in range(start,len(arr)):
        if arr[i] != "C":
            start = i
            break

    #5케이스
    if start == len(arr)-1:
        if arr[start] not in ["A",'B','C','D','E','F']:
            print("Good")
            continue

    elif start == len(arr)-2:
        if arr[start+1] not in ["A",'B','C','D','E','F']:
            print("Good")
            continue

    print("Infected!")

