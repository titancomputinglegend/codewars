def printer_error(s):
    check=list('abcdefghijklm')
    c=0
    for i in range(len(list(s))):
        if s[i] not in check:
            c+=1
    out=str(c)+"/"+str(len(s))
    print(out)



printer_error(s="aaaxbbbbyyhwawiwjjjwwm")