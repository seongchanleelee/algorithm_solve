n = int(input())
pattern = list(input())
left = ''
right = ''
for i in range(len(pattern)):
    if pattern[i] =='*':
        left = ''.join(pattern[0:i])
        right = ''.join(pattern[len(pattern)-1:i:-1])
arr = []
for i in range(n):
    arr.append(input())
for i in range(n):
    if ''.join(arr[i][0:len(left)]) == left and ''.join(arr[i][len(arr[i])-1:len(arr[i])-1-len(right):-1])==right:
        if len(arr[i])-1-len(right)+1 >= len(left):
            print('DA')
        else:
            print('NE')
    else:
        print('NE')

