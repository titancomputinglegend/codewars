def title_case(title, minor_words=''):
    x=(title.lower()).split(" ")
    out=[]
    temp=[]

    for i in range(len(x)):
        temp=list(x[i])
        temp[0]=temp[0].upper()

        out.append("".join(temp))
        temp=[]
        
    return(" ".join(out))
        

    
    
    
def us(usd):
    x="{a} Chinese Yuan".format(a=usd*6.75)
    return(x)

us(5)
