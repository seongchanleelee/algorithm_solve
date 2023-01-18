t = int(input())
for tc in range(t):
    n, k =list(map(int,input().split())) # n: 행성수 k: 함선 수
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    cnt = 0
    yn = False
    while arr !=[]:

        if yn ==True:
            break
        for i in range(len(arr)):
            Sum = sum(arr)
            if Sum <=k:
                yn = True
                break
            if arr[i] <= k:
                k = k + arr[i]
                cnt +=1
                arr.pop(i)
                break
            if i ==len(arr)-1 and k <= arr[0]:
                cnt = -1
                yn = True
                break

    print(f"#{tc+1} {cnt}")