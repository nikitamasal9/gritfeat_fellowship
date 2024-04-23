def reArrange(lst, a):
    finalLst = []
    finalLst = lst[a+1:] + lst[:a+1]
    return finalLst

nums = [1,2,3,4,5,6,7]
k = 3
result = reArrange(nums, k)
print(result)    