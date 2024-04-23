class MergeSort:
    '''
    A class to perform Merge Sort on a given array.
    '''
    def __init__(self, arr):
        '''
        Initializing the MergeSort object with the input array.

        Args:
            arr (list): The array to be sorted.
        '''
        self.arr = arr

    def sorting(self):
        '''
        Sorting the array using the Merge Sort algorithm.
        '''
        if len(self.arr) > 1:
            mid = len(self.arr) // 2
            left_half = self.arr[:mid]
            right_half = self.arr[mid:]

            # Recursively sorting the left and right halves
            left_sorter = MergeSort(left_half)
            left_sorter.sorting()
            right_sorter = MergeSort(right_half)
            right_sorter.sorting()

            # Merging the sorted halves
            self.arrangeMerge(left_sorter.arr, right_sorter.arr)

    def arrangeMerge(self, left, right):
        '''
        Merging two sorted arrays into a single sorted array.

        Args:
            left (list): The left half of the array.
            right (list): The right half of the array.
        '''
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                self.arr[k] = left[i]
                i += 1
            else:
                self.arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            self.arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            self.arr[k] = right[j]
            j += 1
            k += 1

    def display(self):
        '''
        Displaying the sorted array
        '''
        print("Sorted array is:", self.arr)


# Testing:
arr = [60, 20, 40, 10, 90, 30, 80, 50]
sorter = MergeSort(arr)
sorter.sorting()
sorter.display()
