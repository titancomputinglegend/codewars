def digitize(n):
    main=[]

    x=list(str(n))
    x.reverse()
    '''test python'''
#hu

    for i in range(len(x)):
        main.append(int(x[i]))
    return main
    

print(digitize(45762893920))