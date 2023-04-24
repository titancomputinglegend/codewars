def flatten_and_sort(*asrgs):
    out=[]
    if asrgs!=[]:
        for i in range(len(asrgs)):
            if asrgs[i]!=[]:
                for j in range(len(asrgs[i])):
                    if asrgs[i][j]!=[]:
                        out.append(asrgs[i][j])

        return (list(set(out)))
    else:
        return []

print(flatten_and_sort([[]]))