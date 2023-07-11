def generate_hashtag(s):
    out=[]
    s=s.lower()
    if s=='':
        return False
    else:
        s=s.strip()
        s="".join(list(s)).split()
        
        for i in range(len(s)):
            temp=list(s[i])
            temp[0]=temp[0].upper()
            out.append("".join(temp))
            temp=[]

        s="#"+"".join(out)
        if len(s)>140:
            return False
        else:
            return s
print(generate_hashtag(" CoDeWaRs is niCe"))