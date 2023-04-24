def capitals(word):
    #your code here
    final=[]
    out=[]
    for i in word:
        out.append(i.lower())
    word=list(word)
    for i in range(len(word)):
        if word[i]==out[i].upper():
            final.append(i)
    return(final)


capitals('CodEWaRs')