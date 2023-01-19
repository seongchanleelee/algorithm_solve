directy = [0, 0, 1, 1]
directx = [0, 1, 0, 1]

directy = []
for i in range(2):
    directy += [i]*2
print(directy)
directx = []
m =3
for i in range(m):
    for j in range(m):
        directx.append(j)
print(directx)