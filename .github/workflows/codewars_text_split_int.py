def sum_of_integers_in_string(s):
    num=list('0123456789')
    out=["!"]
    s=list(s)
    main=[]

    for i in range(len(s)):
        if s[i] in num:
            out.append(s[i])
        else:
            out.append("!")
    p=("".join(out).split("!"))

    for i in range(len(p)):
        if p[i]!="":
            main.append(p[i])

    main=list(map(lambda x:int(x),main))
    return sum(main)


print(sum_of_integers_in_string("testme94here90donetest988"))