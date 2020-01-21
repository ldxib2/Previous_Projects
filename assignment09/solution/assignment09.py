# Exercise 2
# 2 a)

import random

example1 = [4, 22, 45, 20, 60, 37, 7, 43, 100]
example2 = [4, 1, 2, 1, 3]


def partition(lst, start, end):
    """Function that arranges all values smaller than pivot to left and
     larger values to the right"""

    pivot = lst[start] # pivot is the first value in sequence
    leftmark = start + 1 # define leftmark, closest value to pivot
    rightmark = end  # index of last element in list

    while True:
        while leftmark <= rightmark and lst[rightmark] >= pivot: # move markers inwards until
            # a value that needs reshuffling is found
            rightmark -= 1

        while leftmark <= rightmark and lst[leftmark] <= pivot:
            leftmark += 1

        if leftmark <= rightmark:
            lst[leftmark], lst[rightmark] = lst[rightmark], lst[leftmark]
            # swap the two elements identified as needing reshuffling

        else:
            break

    lst[start], lst[rightmark] = lst[rightmark], lst[start]
    # this swaps the pivot with the right mark element

    return rightmark # this returns the pivot index



def quicksort2(lst, start, end):
    """Function that partitions the input list and recursively quicksorts
    sublists"""

    if start >= end: # recursion beginning
        return lst

    p = partition(lst, start, end)  # partition function
    quicksort2(lst, start, p-1)  # recursion steps
    quicksort2(lst, p+1, end)

    return lst

# Exercise 2 b)

def quicksort(lst):
    """Interface function that shuffles the list and then calls the quicksort
     with the correct start / end values"""

    random.shuffle(lst) # this improves average efficiency
    return quicksort2(lst, 0, len(lst)-1)


# Explanation for randomisation on pdf

print(quicksort(example1))
print(quicksort(example2))