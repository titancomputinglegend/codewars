def no_boring_zeros(n):
    # your code
    x=list(str(n))
    x.reverse()
    ind=0
    for i in range(len(x)):
        if int(x[i])!=0:
            ind=i
            break
    out=x[ind::]
    out.reverse()
    return int("".join(str(x) for x in out))

print(no_boring_zeros(1050))