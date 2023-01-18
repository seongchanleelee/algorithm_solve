t = int(input())
abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for tc in range(1,t+1):
    arr = list(input())
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == abc[i]:
            cnt+=1
        else:
            break
    print(f"#{tc} {cnt}")