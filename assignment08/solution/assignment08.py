import unittest
import time

## Exercise 1

def sieve(n):
    """Algorithm to find primes by eliminating multiples iteratively
    and saving primes and non-primes as dictionary"""
    start_time = time.time() # starts timer for the main body of the function
    sieve = {"prime": [], "non-prime": []}
    numbers = list(range(2, n + 1))  # creates list of numbers from 2 to n
    for i in numbers:
        f = 2  # starting value f
        while i * f <= n:
            if i * f in numbers:
                numbers.remove(i * f)
                sieve["non-prime"].append(i * f)
            f += 1
    sieve["prime"] = numbers

    end_time = time.time() # ends timer of function
    print("Total time: %0.5f"%(end_time - start_time)) # calculates overall time of function

    return sieve



## 1b)

print(sieve(1000))
print('\n')
print(sieve(10000)) # from the times produced by the time function we can
# see that when n = 10000 it took over a hundred times the duration of n = 1000


## 1c)

class Testsieve(unittest.TestCase):
    """Unit test to check the accuracy of sieve function"""
    def setUp(self): # This processes the file used for checking
        with open("primes_check.txt", "r") as f:
            primes_check = f.readlines()
            primes = primes_check[1].split(",")
            non_primes = primes_check[3].split(",")
            primes.remove("\n")
            self.primes = [int(i) for i in primes]
            non_primes.remove('')
            self.nonprimes = [int(i) for i in non_primes]

    def test_sieve(self):
        result = sieve(200)
        self.assertCountEqual(result["prime"], self.primes)
        self.assertCountEqual(result["non-prime"], self.nonprimes) # use CountEqual as the non-prime list is unsorted

## 1d) on pdf file



## Exercise 2a)

def mergesort(lst):
    """Algorithm to order a list using the mergesort process of seperating and
    rebuilding the elements"""
    if len(lst) <= 1: # As this is a recursive function this provides halting mechanism
        return lst

    mid = int(len(lst) / 2)
    left = mergesort(lst[:mid]) # performs the same merging process on the split list
    right = mergesort(lst[mid:]) # as this is recursive it breaks each sublist down until single
    i, j, d = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # compares lowest value of each list and adds it
            lst[d] = left[i]
            i+=1
        else:
            lst[d] = right[j]
            j+=1
        d += 1

    while i < len(left):
        lst[d] = left[i]
        i += 1
        d += 1
    while j < len(right):
        lst[d] = right[j]
        j += 1
        d += 1

    return lst

example_lst = [5, 6, 2, 48, 56, 88, -1, 2, 4, 5] #n little test of the funciton
print(mergesort(example_lst))


## 2b)


def search(n, x):  # assumes a sorted list
    """Combines previous mergesort function with binary search to sort a list
    and look for an element within it"""

    data_sorted = mergesort(x) # previous function
    low = 0
    high = len(data_sorted) - 1

    while low <= high:
        mid = (low + high) // 2
        if n == data_sorted[mid]:
            return True
        elif n < data_sorted[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False

print(search(48, example_lst))


## 2c)

class Testsearch(unittest.TestCase):
    """Unit test to check search function on predetermined lists"""
    def setUp(self):
        self.i = [45, 19187, 232, 8974, 32, 547, 9081, 2, 67, 421]
        self.ii = [345, 10, 754743, 435, 321, 65, 2690, 1234, 5]

    def test_search(self):
        self.assertTrue(search(32, self.i))
        self.assertFalse(search(191, self.ii))

## 2d) - 3b) on pdf


if __name__ == '__main__':
    unittest.main()
#
