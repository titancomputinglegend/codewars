def data_reverse(data):
    out=[]
    temp=[]
    print(len(data))
    x=0
    for i in range(len(data)):
        if x==0:
            temp.append(data[i])
            x+=1
            continue
        if x%8==0:
            print(x)
            out.append(temp)
            temp=[]
            x=0
        else:
            temp.append(data[x])
            x+=1
        
    return out

print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))