def expanded_form(num):
    n=[int(i) for i in (str(num))]
    n.reverse()
    out=[]
    count=10
    for i in range(len(n)):
        if i==0:
            out.append(n[i]*1)
        else:
            out.append(n[i]*(count))
            count=count*10

    out.reverse()


    out=list(filter(lambda x:x!=0,out))
    return " + ".join(str(i) for i in out)

print(expanded_form(4982342))