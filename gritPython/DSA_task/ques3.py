# Question 3
# Write a function that takes a list of digits representing a non-negative integer, increments this integer by 1, and returns the resulting number represented as a list of digits
def increment_integer(digits):
    '''
    Incrementing a non-negative integer represented as a list of digits by 1.
    
    Args:
        digits(list): list of disgits representing a non-negative integer
        
    Returns:
        list: a list of digits after incrementing
    '''
    # Starting with a carry of 1 to increment by 1
    carry = 1  
    # Traversing the digits from right to left
    for i in range(len(digits) - 1, -1, -1):  
        # Adding the carry to the current digit
        digits[i] += carry
        # Updating the carry for the next iteration  
        carry = digits[i] // 10  
        # Updating the current digit to its remainder after division by 10
        digits[i] %= 10 
        # If there's a carry after traversing all digits, adding an additional digit at the beginning.  Otherwise, returning the updated list of digits
    if carry:  
        return [carry] + digits  
    return digits  

# Testing the function
def test_increment():

    # Test case 1
    a1 = [1, 2, 3]
    print("Before incrementing: ", a1)
    result1 = increment_integer(a1)
    print("After incrementing: ", result1)
    try:
        assert result1 == [1, 2, 4]
        print("Test case 1 passed")
    except AssertionError:
        print("Test case 1 failed")

    # Test case 2
    a2 = [1, 2, 9]
    print("Before incrementing: ", a2)
    result2 = increment_integer(a2)
    print("After incrementing: ", result2)
    try:
        assert result2 == [1, 3, 0]
        print("Test case 2 passed")
    except AssertionError:
        print("Test case 2 failed")

    # Test case 3
    a3 = [9, 9, 9]
    print("Before incrementing: ", a3)
    result3 = increment_integer(a3)
    print("After incrementing: ", result3)
    try:
        assert result3 == [1, 0, 0, 0]
        print("Test case 3 passed")
    except AssertionError:
        print("Test case 3 failed")

# Running the tests
test_increment()


