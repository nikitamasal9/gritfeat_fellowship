#Question 2:
#Write a function to find the k-th largest element from a given unsorted array without using any built-in functions. Also write some tests.


def find_kth_largest(arr, k):
    """
    Finding the k-th largest element from a given unsorted array.

    Args:
        arr: The unsorted array.
        k: The value of k for which to find the k-th largest element.

    Returns:
        The k-th largest element.
    """
    # Performing a partition step similar to QuickSort
    def partition(arr, low, high):
        # Choosing the last element as the pivot
        pivot = arr[high]  
         # Indexing of the smaller element
        i = low - 1 
        #iterating and swapping if the current element is less tha or equal to pivot
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        #placing the next element(with index i+1) that places pivot in its correct sorted position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        #returning partition point
        return i + 1

    # Finding the k-th largest element using QuickSelect algorithm
    def quick_select(arr, low, high, k):
        if low <= high:
            # Partitioning the array and get the pivot index
            pivot_index = partition(arr, low, high)

            # If pivot_index is the k-th largest element, return it
            if pivot_index == len(arr) - k:
                return arr[pivot_index]

            # If pivot_index is less than the k-th largest element,
            # search in the right subarray
            elif pivot_index < len(arr) - k:
                return quick_select(arr, pivot_index + 1, high, k)

            # Otherwise, search in the left subarray
            else:
                return quick_select(arr, low, pivot_index - 1, k)

    # Checking if k is valid
    if k <= 0 or k > len(arr):
        return None

    # Calling the quick_select function to find the k-th largest element
    return quick_select(arr, 0, len(arr) - 1, k)


# Testing the function
def test_find_kth_largest():

    # Test case 1
    arr1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print(k1, "th largest element is ", find_kth_largest(arr1, k1))
    try:
        assert find_kth_largest(arr1, k1) == 5
        print("Test case 1 passed")
    except AssertionError:
        print("Test case 1 failed")

    # Test case 2
    arr2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print(k2, "th largest element is ", find_kth_largest(arr2, k2))
    try:
        assert find_kth_largest(arr2, k2) == 4
        print("Test case 2 passed")
    except AssertionError:
        print("Test case 2 failed")

    # Test case 3
    arr3 = [1]
    k3 = 1
    print(k3, "th largest element is ", find_kth_largest(arr3, k3))
    try:
        assert find_kth_largest(arr3, k3) == 1
        print("Test case 3 passed")
    except AssertionError:
        print("Test case 3 failed")

    # Test case 4 (Invalid k)
    arr4 = [1, 2, 3]
    k4 = 0
    print(k4, "th largest element is ", find_kth_largest(arr4, k4))
    try:
        assert find_kth_largest(arr4, k4) == 4
        print("Test case 4 passed")
    except AssertionError:
        print("Test case 4 failed")
    
# Running the tests
test_find_kth_largest()
