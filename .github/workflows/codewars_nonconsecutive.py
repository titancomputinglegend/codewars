#other
def special_number(number):
    p=[int(i) for i in list(str(number))]
    test=[0,1,2,3,4,5]
    check=0
    for i in range(len(p)):
        if p[i] not in test:
            check=0
            break
        else:
            check=1
    if check==0:
        return "NOT!!"
    else:
        return "Special!!"


print(special_number(2))