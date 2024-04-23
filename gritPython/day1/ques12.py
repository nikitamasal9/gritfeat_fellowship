def reArrange(lst, a):
    finalLst = []
    for i in range(a+1, len(lst)):
        finalLst.append(lst[i])
    for j in range(0, a+1):
        finalLst.append(lst[j])
    return finalLst

nums = [1,2,3,4,5,6,7]
k = 3
result = reArrange(nums, k)
print(result)    