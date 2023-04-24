n=25
d=1

sqr=[]
for i in range(0,n+1):
    sqr.append(i)

sqr=list(map(lambda x:x**2,sqr))

count=0
for i in range(len(sqr)):
    for j in str(sqr[i]):
        if j==str(d):
            count+=1
    
print(count)
