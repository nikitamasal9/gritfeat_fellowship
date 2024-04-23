# Question 1:
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# defining the function
def leapYear(year):
    '''
    Determining whether a given year is a leap year or not.

    Args: 
        year(int): the year to be checked.

    Returns:
        bool: True if the given year is a leap year, else False.

    '''
    # Checks condition for leap year: either the given year is evenly divided by 4 and not evenly divided by 100
    if (year % 4) == 0 and (year % 100) != 0:
        return True
    # Checks condition for leap year: either the given year is evenly divided by 100 and 400 or not
    elif (year % 100) == 0 and (year % 400) == 0:
        return True
    else:
        return False
    
# testing the function
yr = int(input("Enter the year: "))
result = leapYear(yr)
print(result)
