while True:
    try:
        t = list(input())
        upper = [0]*len(t)
        for i in range(len(t)):
            if t[i].isupper():
                t[i]=t[i].lower()
                upper[i] = 1
        m = ["a",'i','y','e','o','u','a','i','y']
        j = ["b","k","x","z","n","h","d","c","w","g","p","v","j","q","t","s","r","l","m","f","b","k","x","z","n","h","d","c","w","g"]

        for i in range(len(t)):
            if t[i] in m:
                t[i] = m[m.index(t[i])+3]


            if t[i] in j:
                t[i] = j[j.index(t[i])+10]

        for i in range(len(upper)):
            if upper[i] ==1:
                t[i] = t[i].upper()

        t = ''.join(t)
        print(t)
    except:
        break
