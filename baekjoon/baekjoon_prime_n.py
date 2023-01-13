m,n = list(map(int,input().split()))
prime = []
check = [0]*(n+1)
for i in range(2,n+1):
    if not check[i]:
        prime.append(i)
    for j in range(i+i,n+1,i):
        check[j] = 1
for i in range(len(prime)):
    if m<=prime[i]<=n:
        print(prime[i])