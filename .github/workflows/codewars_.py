def open_or_senior(data):
    out=[]
    for i in range(len(data)):
        if data[i][0]>=55 and data[i][1]>7:
            out.append("Senior")
        else:
            out.append("Open")
    return(out)

x=(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
print(x)