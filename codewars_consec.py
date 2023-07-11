def sum_of_differences(arr):
    if arr==[] or len(arr)==1:
        return 0
    else:
        arr.sort()
        arr.reverse()
        test=[]
        try:
            for i in range(len(arr)):
                test.append(arr[i]-arr[i+1])
        except:
            IndexError()
        return sum(test)

print(sum_of_differences([-3, -2, -1]))