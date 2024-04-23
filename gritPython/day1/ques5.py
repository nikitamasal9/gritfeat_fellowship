# Question 5:
# Write a Python function that takes two sets as arguments and returns a new set containing the elements that are in the first set but not in the second set, and the elements that are in the second set but not in the first set.

# defining the function
def twoSets(set1, set2):
    '''
    Returning a new set containing the elemnts that are unique to each input set.

    Args:
        set1(set): first input set.
        set2(set): second input set.

    Returns:
        finalset(set): A new set containing elements unique to each input sets.
    '''

    # initializing an empty list to store elements unique to each set
    finalSet = []

    # iterating over elements in set1 to append unique element to the final set:
    for x in set1:
        if x not in set2:
            finalSet.append(x)

    # iterating over elements in set2 to append unique element to the final set:
    for y in set2:
        if y not in set1:
            finalSet.append(y)

    # converting list to set
    finalset = set(finalSet)
    return(finalset)

# testing the function
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
result = twoSets(s1,s2)
print(result)
