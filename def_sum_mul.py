def sum_mul(n, m):
    if n>0 and m>0:
        p=[int(i) for i in range(n,m)]
        p=list(filter(lambda x:x%n==0,p))
        return sum(p)
    else:
        return "INVALID"


print(sum_mul(4,123))