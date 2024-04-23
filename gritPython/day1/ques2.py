# Question 2:
# Write a Python function that takes two lists of integers as arguments and returns a new list containing only the numbers that are present in both lists, but with each number appearing only once in the final list.

# defining the function
def listFxn(lst1, lst2):
    '''
    Returning the list containing common elemnts from the given two lists.
    
    Args:
        lst1(list): First input list.
        lst2(list): Second input list.
    
    Returns:
        finalList(list): A list containing elements common to two given lists.
    '''
    
    # initializing empty list
    finalList = [] 
    
    # converting input lists to sets for efficiency
    a = set(lst1)
    b = set(lst2)

    # iterating over elemnts in the first list to check whether each element exists in second list or not
    for x in a:
        if x in b:
            finalList.append(x)
    return(finalList)
    

# testing the function
l1 = [1,2,3,4,5,5]
l2 = [2,3,4,5,6]
result = listFxn(l1, l2)
print(result)