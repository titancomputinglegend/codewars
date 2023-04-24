def series_sum(n):
    # Happy Coding ^_^
    if n > 1 :
        sum=0
        j=4
        for i in range(1,n):
            sum = sum + 1/j
            j=j+3
        
        return str(round(sum+1,2))
    else:
        if n == 0:
            return "0.00"
        elif n==1:
            return "1.00"


def sequence_sum(begin_number, end_number, step):
    #your code here
    if begin_number > end_number :
        return 0
    else:
        sum=0
        for i in range(begin_number,end_number+1, step):
            sum=sum+i  
        return(sum)

def reverse_list(l):
    'return a list with the reverse order of l'
    l.sort()
    l.reverse()
    return(l)


print(reverse_list([3,4,5,1,]))