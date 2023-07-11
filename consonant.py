def solve(s):
    alpha="!bcd!fgh!jklmn!pqrst!vwxyz"
    out=[]
    fin=[]
    temp=[]
    tot=n=0;

    for i in range(len(s)):
        if s[i] not in alpha:
            out.append("!")
        else:
            out.append(s[i])
    p=list("".join(out))
    for i in range(len(p)):
        if p[i]=="!":
            print(True)


(solve("zodiacs"))