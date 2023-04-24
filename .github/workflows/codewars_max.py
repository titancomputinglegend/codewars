def sum_array(arr):
    #your code here
    arr.sort()
    arr.pop(0);arr.pop(-1)
    return(sum(arr))

sum_array([6, 2, 1, 8, 10])