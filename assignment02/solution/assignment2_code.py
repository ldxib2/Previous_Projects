# Exercise 4

even_fct = lambda x: x % 2 == 0


# Input array
input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(input_array)

# Testing function with input_array
print(list(filter(lambda x: x % 2 == 0, input_array)))


# Exercise 5

def remove_long_words(s, n):
    list = (s).split()
    list_edit = [element for element in list if len(element) <= n]
    return print(list_edit)

sentence = "The Day of the Jackal"


remove_long_words(sentence, 3)