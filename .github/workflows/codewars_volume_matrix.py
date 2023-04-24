def find_difference(a, b):
    # Your code here!
    a="{x}*{y}*{z}".format(x=a[0],y=a[1],z=a[2])
    b="{x}*{y}*{z}".format(x=b[0],y=b[1],z=b[2])

    a,b=eval(a),eval(b)
    if a>b:
        return a-b
    else:
        return b-a

find_difference([2,2,3],[5,4,1])