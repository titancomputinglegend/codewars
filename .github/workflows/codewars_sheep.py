def count_sheep(n):
    x=[]
    for i in range(1, n+1):
        x.append("{m} sheep...".format(m=i))
    return("".join(x))

print(count_sheep(5))