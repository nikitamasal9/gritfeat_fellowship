class SelectionSort:
    '''
    A class to perform Selection Sort on a given array.
    '''
    def __init__(self, arr):
        '''
        Initializing the SelectionSort object with the input array.

        Args:
            arr (list): The array to be sorted.'''
        self.arr = arr

    def selection(self):
        '''
        Sorting the array using the Selection Sort algorithm.
        '''
        n = len(self.arr)
        for i in range(n):
            mini = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[mini]:
                    mini = j
            self.arr[i], self.arr[mini] = self.arr[mini], self.arr[i]

    def display(self):
        '''
        Displaying the sorted array.
        '''
        print("Sorted array is:", self.arr)


# Testing:
arr = [10, 19, 9, 2, 79, 99, 84, 28, 14, 20]
arrange = SelectionSort(arr)
arrange.selection()
arrange.display()
