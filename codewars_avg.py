def better_than_average(class_points, your_points):
    # Your code here

    if sum(class_points)//len(class_points)<your_points:
        return True
    else:
        return False

better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)