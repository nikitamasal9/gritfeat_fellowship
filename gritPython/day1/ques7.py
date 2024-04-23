# Question 7:
# Write a Python program that takes a list of tuples, where each tuple contains a string and an integer, and returns a new list containing the tuples sorted by the length of the string, with ties broken by the value of the integer.

# defining the function
def sortTuples(tuplesList):
    '''
    Returning a new list containing tuples sorted by the length of the string with ties broken by value of the integer
    
    Args:
        tuplesList(list of tuples): input list of tuples, where each tuple contains a string and an integer
        
    Returns:
        list of tuples: A new list containing tuples sorted by length of the string where ties are broken by the value of the integer.
    '''

    # Use the sorted() function with a custom key function to sort the list of tuples
    # The key function sorts tuples by the length of the string first (index 0), then by the integer value (index 1)
    return sorted(tuplesList, key=lambda x: (len(x[0]), x[1]))

# testing the function
inputList = [("apple", 3), ("banana", 2), ("pear", 5), ("kiwi", 2), ("orange", 3), ("grape", 4)]
result = sortTuples(inputList)
print(result)
