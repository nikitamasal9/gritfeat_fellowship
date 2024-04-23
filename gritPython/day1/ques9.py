# Question 9:
# Write a Python function that takes a list of tuples, where each tuple contains a string and a set of integers, and returns a new list containing the tuples sorted by the sum of the integers in the set, with ties broken by the length of the string.

# defining the function
def sortTuples(tuplesList):
    '''
     Returning a new list containing tuples sorted by the sum of integers in the set with ties broken by length of the string.
    
    Args:
        tuplesList(list of tuples): input list of tuples, where each tuple contains a string and a set of integers.
        
    Returns:
        list of tuples: A new list containing tuples sorted by sum of integers where ties are broken by length of string.
    '''
    # Use the sorted() function with a custom key function to sort the list of tuples
    # The key function sorts tuples by the sum of integers in the set first, then by the length of the string
    return sorted(tuplesList, key=lambda x: (sum(x[1]), len(x[0])))

# testing the function
inputList = [("apple", {3, 2}), ("banana", {2, 1}), ("pear", {4, 1}), ("kiwi", {2, 1}), ("orange", {3, 3}), ("grape", {4, 3})]
result = sortTuples(inputList)
print(result)
