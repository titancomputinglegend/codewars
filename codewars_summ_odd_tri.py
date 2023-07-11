def row_sum_odd_numbers(n):
    #your code here
    p=n*(n-1)+1
    num=[]
    for i in range(n):
        num.append(p)
        p+=2
    return sum(num)

print(row_sum_odd_numbers(3))
