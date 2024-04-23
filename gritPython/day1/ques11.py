# Question 11:
# Write a Python function that takes a list of tuples, where each tuple contains a string and a list of integers, and returns a new list containing the tuples sorted by the median of the integers in the list, with ties broken by the length of the string

# importing statistics module to calculate median
import statistics

# defining the function
def sortTuples(tuplesList):
    '''
     Returning a new list containing tuples sorted by the median of integers in the list with ties broken by length of the string.
    
    Args:
        tuplesList(list of tuples): input list of tuples, where each tuple contains a string and a list of integers.
        
    Returns:
        list of tuples: A new list containing tuples sorted by median of integers where ties are broken by length of string.
    '''
    # Use the sorted() function with a custom key function to sort the list of tuples
    # The key function sorts tuples by the median of integers in the list first, then by the length of the string
    return sorted(tuplesList, key=lambda x: (statistics.median(x[1]), len(x[0])))

# testing the function
inputList = [("apple", [3, 2]), ("banana", [2, 1]), ("pear", [4, 1]), ("kiwi", [2, 1]), ("orange", [3, 3]), ("grape", [4, 3])]
result = sortTuples(inputList)
print(result)
