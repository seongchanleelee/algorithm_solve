s = list(input())
t = list(input())
result = 0
while 1:
    if s ==t:
        result = 1
        break
    if len(s) == len(t) and s != t:
        result = 0
        break
    if t[-1] == 'A':
        t.pop(-1)
        continue

    if t[-1] == 'B':
        t.pop(-1)
        t.reverse()
print(result)
