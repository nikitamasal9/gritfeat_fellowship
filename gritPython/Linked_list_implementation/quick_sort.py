class QuickSort:
    '''
    A class to perform Quick Sort on a given array.
    '''
    def __init__(self, arr):
        '''
        Initializing the QuickSort object with the input array.

        Args:
            arr (list): The array to be sorted.
        '''
        self.arr = arr

    def sort(self):
        '''
        Initiating the Quick Sort algorithm on the array.
        '''
        self.quickSort(0, len(self.arr) - 1)

    def quickSort(self, low, high):
        '''
        Recursively sorting the array using the Quick Sort algorithm.

        Args:
            low (int): The starting index of the subarray to be sorted.
            high (int): The ending index of the subarray to be sorted.
        '''
        if low < high:
            pivot = self.partition(low, high)
            self.quickSort(low, pivot - 1)
            self.quickSort(pivot + 1, high)

    def partition(self, low, high):
        '''
        Partitioning the array around a pivot element.

        Args:
            low (int): The starting index of the subarray to be partitioned.
            high (int): The ending index of the subarray to be partitioned.

        Returns:
            int: The index of the pivot element after partitioning.
        '''
        p = self.arr[low]
        i = low + 1
        j = high

        while True:
            while i <= j and self.arr[i] <= p:
                i += 1
            while i <= j and self.arr[j] > p:
                j -= 1
            if i <= j:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            else:
                break

        self.arr[low], self.arr[j] = self.arr[j], self.arr[low]
        return j

    def display(self):
        '''
        Displaying the sorted array.
        '''
        print("Sorted array is:", self.arr)


# Testing:
arr = [5, 8, 1, 2, 6, 3, 9]
sorter = QuickSort(arr)
sorter.sort()
sorter.display()
