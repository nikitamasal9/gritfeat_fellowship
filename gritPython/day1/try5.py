# Question 5: Alterantive
# Write a Python function that takes two sets as arguments and returns a new set containing the elements that are in the first set but not in the second set, and the elements that are in the second set but not in the first set.

# defining the function
def twoSets(set1, set2):
    '''
    Returning a new set containing the symmetric difference of two input sets.
    
    Args:
        set1(set): first input set.
        set2(set): second input set.

    Returns:
        set: A new set containing elements that are not common to set1 and set2.
    '''
    return(set1 ^ set2)

# testing the function
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
result = twoSets(s1,s2)
print(result)
