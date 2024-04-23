# Question 8:
# Write a Python function that takes a dictionary as an argument and returns a new dictionary where the keys are sorted alphabetically and the values are sorted in descending order.

# defining the function
def sortDict(dictionary):
    '''
    Returning a new dictionary where the keys are sorted alphabetically and the values are in descending order
    
    Args:
        dictionary(Dict): input dictionary
        
    Returns:
        sortedDict(Dict): A new dictionary with keys sorted alphabetically and values sorted in descending order.'''
    
    # sorting keys alphabetically
    sortedKeys = sorted(dictionary.keys())

    # sorting values in descending order
    sortedValues = sorted(dictionary.values(), reverse=True)

    # creating a new dictionary by pairing sorted keys with sorted values
    sortedDict = {key: value for key, value in zip(sortedKeys, sortedValues)}
    return sortedDict

# testing the function
inputDict = {'banana': 5, 'apple': 10, 'orange': 3, 'grape': 8}
result = sortDict(inputDict)
print(result)
