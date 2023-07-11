def same_case(a, b): 
    # your code here
    al="qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
    if a in al and b in al:
        if a.upper()==a and b.upper()==b:
            return 1
        else:
            return 0
    else:
        return -1
    

print(same_case("b","A"))