import sys
input = sys.stdin.readline

m,n,k = list(map(int,input().split()))
arrm = list(map(int,input().split()))
arrn = list(map(int,input().split()))
for i in range(len(arrn)):
    if arrn[i] == arrm[0]:
        if len(arrn) >=i + len(arrm):
            if arrn[i:i+len(arrm)] == arrm:
                print("secret")
                sys.exit()
print("normal")


