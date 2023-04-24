def capitalize(s):
    s=list(s)
    even=[]
    odd=[]
    for i in range(len(s)):
        if i%2==0:
            even.append(s[i].upper())
        else:
            even.append(s[i])
    for i in range(len(s)):
        if i%2==1:
            odd.append(s[i].upper())
        else:
            odd.append(s[i])

    even=str("".join(even))
    odd=str("".join(odd))
    out=[]
    out[0:2]=even, odd
    return(out)

capitalize('abcdef')