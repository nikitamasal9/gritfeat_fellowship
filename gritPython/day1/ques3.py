# Question 3:
# Write a Python function that takes a string as an argument and returns a dictionary where each key is a unique word in the string and the value is a list of the indices where that word appears in the string.

# defining the function
def wordIndices(str):
    '''
    Returning a dictionary where eack key is a unique word in the string and the value is a list of indices where that word appears.

    Args:
        str(string): Input string.

    Returns:
        wordDict(Dict): A dictionary where keys are unique words and values are lists of indices where each word appears.
    '''
    # Initializing an empty dictionary to store word indices
    wordDict = {}

    # splitting the given string into words
    words = str.split()

    # iterating over words and their indices
    for index, word in enumerate(words):
        # if the word is not in the dictionary, ad it with the current index as a list, else append the current index to its list
        if word not in wordDict:
            wordDict[word] = [index]
        else:
            wordDict[word].append(index)
    return wordDict

# testing the function
text = "apple banana apple kiwi grapes banana kiwi"
result = wordIndices(text)
print(result)
