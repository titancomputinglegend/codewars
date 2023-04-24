def tower_builder(n_floors):
    # build here
    out=[]
    count=1
    for i in range(n_floors):
        print("*"*count,end="")
        count=count+2
        
tower_builder(6)