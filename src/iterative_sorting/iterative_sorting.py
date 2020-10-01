# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # for x in the range of the current index + 1 (moving right) within the array:
        for smallest_index in range(i + 1, len(arr)):
            # if the smallest index in the array is lower than x in the array:
            if arr[smallest_index] < arr[cur_index]:
                # the smallest index is equal to x
                cur_index = smallest_index

        # TO-DO: swap
        # Your code here
        # current index in the array is now the smallest index in the array
            arr[i], arr[cur_index] = arr[cur_index], arr[i]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    # length is the length of the array
    length = len(arr)
    # for i in the range of the length
    for i in range(length):
        # boolean swapped variable that is set to false
        swapped: bool = False

        compared_range = length - i - 1
        # for x in the range of the array -1 (moving left) of the current index:
        for x in range(0, compared_range) :
            # next index is current index + 1 (moving right)
            next_index = x + 1
            # if x index is lower than the next index
            if arr[x] > arr[next_index]:
                # swap values
                arr[x], arr[next_index] = arr[next_index], arr[x]
                # swapped is set to true
                swapped = True
    # if swapped is equal to false function stops
            elif swapped == False:
                pass      


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
