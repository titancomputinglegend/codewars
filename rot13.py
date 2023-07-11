def rot13(message):
    m=message
    out=[]
    a="abcdefghijklmnopqrstuvwxyz"

       
    for i in range(len(m)):
        n=0
        if m[i] in a or m[i].lower() in a:
            if m[i]==m[i].lower():
                n=a.index(m[i])+13
                if n>25:
                    n=n-25-1
                out.append(a[n])
            elif m[i]==m[i].upper():
                n=a.index(m[i].lower())+13
                if n>25:
                    n=n-25-1
                out.append(a[n].upper())


        else:
            out.append(m[i])
    return "".join(out)

print(rot13("Test& "))