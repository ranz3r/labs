def uniq(lst):
    newlst = []
    for i in lst:
        if ((lst[i] in newlst)==False):
            newlst.append(lst[i])
    return newlst

maxlist = [1 , 1, 1, 5 , 5, 6, 3, 7, 5]
print(uniq(maxlist))
