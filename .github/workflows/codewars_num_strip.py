def string_clean(s):
    """
    Function will return the cleaned string
    """
    s=list(s)
    out=[]
    
    for i in range(len(s)):
        try:
            s[i]=int(s[i])
        except:
            out.append(s[i])
            ValueError
    # Your code here
    return("".join(out))
string_clean("(E3at m2e2!!)")