def move_zeros(lst):
    for i in range(len(lst)):
        if lst[i]==0:
            lst.remove(0)
            lst.append(0)
    return lst


print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))