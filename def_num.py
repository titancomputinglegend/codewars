a=open("output.txt","w")
def test(x,y):
    for i in range(x+1,y):
        a.write(str(i)+"\n")

test(3,10)