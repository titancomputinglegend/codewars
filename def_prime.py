def t(n):
    check="Yes"
    if n<=1:
        check="No"
    else:
        for i in range(2,n):
            if n%i==0:
                check="No"
                break
    return check

def prime(x,y):
    for i in range(x,y+1):
        if t(i)=="Yes":
            print(i)
    
prime(0,20) #Example