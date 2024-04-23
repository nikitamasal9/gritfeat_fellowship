# Question 6:
# Write a Python function that takes a list of strings as argument and returns a new list containing only the strings that are palindromes.

# defining the function
def palindromeString(str1):
    '''
    Returning a new list containing only the strings that are palindrome.
    
    Args:
        str1(string): input string
        
    Returns:
        finalList(list): A new list containing only palindrome strings'''
    
    # initializing an empty list to store palindrome strings.
    finalList = []

    # splitting input string into words
    words = str1.split(" ")

    # iterating over each word in the list
    for word in words:
        # checking if the word is palindrome. If palindrome, append it to the final list
        if word == word[::-1]:
            finalList.append(word)
    return finalList

# testing the function
st = "abba aabbb aabbaa abababab abbbba"
result = palindromeString(st)
print(result)

