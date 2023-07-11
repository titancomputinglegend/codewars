x="t1est11101"
x=list(x)
count=0
for i in range(len(x)):
    try:
        if type(int(x[i]))==int:
            count+=1
    except:
        TypeError
print(count)