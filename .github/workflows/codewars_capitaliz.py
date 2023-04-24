def accum(s):
    s=list(s)
    temp=[]
    out=[]
    for i in range(len(s)):
        s[i]=s[i].upper()+s[i]*i

  

    return("-".join(s))

def replace_all(obj, find, replace):
    if type(obj)==str:
        obj=obj.replace(find,replace)
        return(obj)
    else:
        for i in range(len(obj)):
            if obj[i]==find:
                obj[i]=replace
        return obj

print(replace_all([3,4,4,41],4,1))