# Question 4:
# Write a Python function that takes a list of integers as argument and returns a new list with the elements sorted in descending order, but with all odd numbers appearing before all even numbers.

# defining the function
def oddEven(lst):
    '''
    Returning a new list with the elements stored in descending order, where odd numbers are before even numbers.

    Args:
        lst(list): input list of integers.

    Returns:
        finallst(list): a list with elemenst sorted in descending order, odd numbers appearing before even numbers.
    '''

    # initializing lists to store even and odd numbers
    evenlst = []
    finallst = []

    # iterating over elements in the given list
    for x in lst:
        # separating odd and even numbers and appending in the lists accordingly
        if (x % 2) == 0:
            evenlst.append(x)
        else:
            finallst.append(x)
        # sorting the lists in descending order
        evenlst.sort(reverse=True)
        finallst.sort(reverse=True)
    # concatenating odd numbers' list followed by even numbers' list
    finallst.extend(evenlst)
    return finallst

# testing the function
lst = [1,2,3,4,5,89,54,67,31,76,92]
result = oddEven(lst)
print(result)

