

import math
#######################################################

####   Exercise 2. a) SOLUTION


def decimal_to_octal(n):
    # function to convert decimal integers to binary
    x = []
    while n > 0:
        x.insert(0, str(n % 8))
        n = math.floor(n / 8) # algorithm adds each calculation to list
    if x == []:
        x.append(0) # extra code for including 0

    x_pretty = ''.join(str(n) for n in x) # not necessary but adds readability

    return x_pretty

print(decimal_to_octal(0))
print(decimal_to_octal(17))
print("\n") # line break for readability


#### Exercise 2. b) SOLUTION

# function for changing decimal numbers with decimal places to octal
def decimal_to_octal(n):
    i = int(n)
    d = n - int(n) # way of separating the integer and decimal place values of number
    x = []
    while True:
        x.insert(0, str(i % 8))
        i = math.floor(i / 8)
        if i == 0:
            break

    if d != 0:
        x.append(".") # this makes the number read as a decimal place when needed

    if d > 0:
        while True:
            x.append(str(int(d*8)))
            d = d*8 - (int(d*8))
            if d*8 - (int(d*8)) == 0:
                break

    x_pretty = ''.join(e for e in x) # again for readability



    return print(x_pretty)

decimal_to_octal(17)
decimal_to_octal(0)
decimal_to_octal(17.25)
print("\n")

########## Exercise 3 a)

import unittest

def decimal2binary(n):
    # function to convert decimal integers to binary from assignment
    x = []
    while n > 0:
        x.append(n % 2)
        n = math.floor(n/2)
    return x[::-1] # this inverts the list to make the order correct


print(decimal2binary(2))
print("\n")


class TestD2B(unittest.TestCase):
    def test_decimal2binary(self):
        # for n_attempt in range(-1, 3)
        # Issue of what is expected here as the notation is vital for negative numbers.
        # For positive numbers we can just use the bits necessary whereas for negatives/
        # this provides insufficient information as can be seen from the test for (-1)
        self.assertEqual(decimal2binary(-1), [1, 1, 1, 0])
        self.assertEqual(decimal2binary(0), [0])
        self.assertEqual(decimal2binary(1), [1])
        self.assertEqual(decimal2binary(2), [1, 0])
        self.assertEqual(decimal2binary(3), [1, 1])


########### Exercise 3 b)

def decimal_to_binary_correct(n):
    # function to convert decimal integers to binary
    y = []
    x = n

    if n == 0: # this is just to accommodate for 0. This could also be represented using 1s
        y.append(0)

    while n > 0: # algorithm first deals with positive numbers
        y.insert(0, (n % 2))
        n = math.floor(n / 2)


    if n < 0: # now deals with negative numbers
        n = n * -1 # conversion to positive
        while n > 0:
            y.insert(0, (n % 2)) # insert function allows for correct ordering
            n = math.floor(n / 2)

        for n in range(0, len(y)): # this provides the inversion necessary for one's complement
            if y[n] >= 0:
                y[n] = 1 - y[n]

    while len(y) % 8 != 0: # this adds in either 0s or 1s to standardize an 8-bit\
                           # or higher notation
        if x >= 0:
            y.insert(0, 0) # for positive numbers
        else:
            y.insert(0, 1) # for negative numbers

    # y_pretty = ''.join(str(e) for e in y)
    # we could use the line above to convert the output from a list to a string\
    # which would make the output more readable. I have opted to keep the list function\
    # for uniformity with the first test.

    return y


print(decimal_to_binary_correct(1))
print(decimal_to_binary_correct(-1))
print("\n")
print(decimal_to_binary_correct(27))
print(decimal_to_binary_correct(-27))
print("\n")
print(decimal_to_binary_correct(0))


class TestDecimal2Binary(unittest.TestCase):
    def test_decimal_to_binary_correct(self):
        # for n_attempt in range(-1, 3)
        # for this test we are assuming that the output always takes 8-bit notation\
        # or multiples of 8 i.e. 16, 24, 32 bit notation\
        # therefore is we want to test an output we expect to be 29 bits we make\
        # this up to 32 bits by adding 1s or 0s at the start of the number\
        # for negative or positive numbers respectively
        self.assertEqual(decimal_to_binary_correct(-1), [1, 1, 1, 1, 1, 1, 1, 0])
        self.assertEqual(decimal_to_binary_correct(0), [0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(decimal_to_binary_correct(1), [0, 0, 0, 0, 0, 0, 0, 1])
        self.assertEqual(decimal_to_binary_correct(2), [0, 0, 0, 0, 0, 0, 1, 0])
        self.assertEqual(decimal_to_binary_correct(3), [0, 0, 0, 0, 0, 0, 1, 1])


if __name__ == '__main__':
    unittest.main()




