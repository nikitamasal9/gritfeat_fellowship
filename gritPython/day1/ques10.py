# Question 10:
# Write a Python function that takes a string as an argument and returns a new string where each word in the string is replaced with the word that appears most frequently in the string.

# defining the function:
def frequent(str):
    '''
    Returning a new string where each word in the input string is replaced with the word that appears most frequently.
    
    Args:
        str(string): input string
        
    Returns:
        output(string): A new string with each word replaced by the word that appears most frequently.'''
    
    # Splitting the input string into words and convert them to lowercase
    words = str.lower().split(" ")

    # Creating a dictionary to store word frequencies
    wordCountDict = {} 

    for word in words:
        # Counting the frequency of each word and store it in the dictionary
        if word not in wordCountDict:
            wordCountDict[word] = words.count(word)
    
    # Finding the word that appears most frequently
    mostFreq = max(wordCountDict, key= lambda x: wordCountDict[x])
    
    # Creating the output string by repeating the most frequent word for each word in the original string
    output = (mostFreq + " ") * len(words)
    return output

# testing the function
txt = "this is question num ten in basic python programming . Python is a high-level , python is also a general-purpose programming language"
result = frequent(txt)
print(result)
