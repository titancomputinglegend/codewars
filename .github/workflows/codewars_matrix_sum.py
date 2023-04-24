def sum_of_minimums(numbers):
    out=[]
    for i in range(len(numbers)):
        out.append(min(numbers[i]))
    return(sum(out))
sum_of_minimums([[ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5]])