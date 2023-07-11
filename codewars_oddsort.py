def sort_array(source_array):
    # Return a sorted array.
    out=[]
    p=0
    
    x=sorted(source_array)

    for i in range(len(x)):
        if x[i]%2 == 1:
            out.append(x[i])
    
    for i in range(len(x)):
            if x[i]%2==1:
                if p<=len(out):
                    x[i]=out[p]
                    p=p+1
    print(x)


sort_array([5, 3, 2, 8, 1, 4])