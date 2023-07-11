def find_outlier(integers):
    x=list(filter(lambda x:x%2==0,integers))
    y=list(filter(lambda x:x%2==1,integers))

    if len(x)==1:
        return x[0]
    else:
        return y[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))