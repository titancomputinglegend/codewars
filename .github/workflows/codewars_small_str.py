def find_short(s):
    # your code here
    max=0
    y = s.split()
    out=[]

    for i in range(len(y)):
        out.append(len(y[i]))
    out.sort()
    return  (out[0])
        

    
(find_short("bitcoin take over the world maybe who knows perhaps"))