st = 2
for i in range(2):
    for j in range(10):
        for k in range(st,st+4):
            print(f'{k} * {j} = {k*j}',end=' ')
        print()
    st = 6
    print()