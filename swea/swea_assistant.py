t = int(input())
for tc in range(1, t+1):
    n,k = list(map(int,input().split()))
    arr = [list(map(int,input().split()))for _ in range(n)]

    student = [0]*n
    point = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
    grades = []
    for i in range(len(arr)):
        student[i] = arr[i][0]*35 + arr[i][1]*45 + arr[i][2]*20
    # student.sort(reverse=True)


    st = 0
    for i in range(len(point)):
        grades.append(point[i]*(n//len(point)))
    print(f'#{tc} {grades[k]}')
