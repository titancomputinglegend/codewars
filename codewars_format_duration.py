def format_duration(s):
    month=minute=days=years=hours=0
    out=[]
    #your code here
    while s>=60:  #minute check
        minute+=1
        s-=60
    while minute >=60:
        hours+=1
        minute-=60
        
    while hours>=24:
        days+=1
        hours-=24
    while month>=12:
        years+=1
        month-=12

    if s==0:
        return "Now"
    else:
        if s==0:
            if minute==0:
                if hours==0:
                    if days==0:
                        pass
                    else:
                        out.append(str(str(days)+" Days, "))
                else:
                    out.append(str(str(hours)+" Hours, "))
            else:
                out.append(str(minute)+"Minute")
        else:
            out.append(str(s)+"seconds") 
    return out
print(format_duration(86459))