def array_diff(a, b):
    #your code here
    out = []
    for i in range(len(a)):
        if a[i] in b:
            continue
        else:
            out.append(a[i])
    return(out)


(array_diff([1,2,3], [1, 2]))