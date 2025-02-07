def spy_game(nums):
    spy = [0,0,7]
    x=0
    for i in nums:
        if i==spy[x]:
            x+=1
        if x == len(spy):
            return print("True")
    return print("False")
spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0]) 