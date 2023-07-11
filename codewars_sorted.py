def is_sorted_and_how(arr):
 

    a=arr.copy()
    d=arr.copy()
    a.sort()
    d.sort()
    d.reverse()

    if arr==a:
        return ""
    elif arr==d:
        state="Dsc"
    else:
        state="No"
    return (state) 

is_sorted_and_how([3,12,3])