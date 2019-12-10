
# Exercise 1

import csv

def import_csv(filepath):
    """General function for importing and reading csv files. This parses the
    data into a nested list, first index is each row and second index
    is each variable"""

    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        new_csv = [line for line in csv_reader] #list comprehension to create new object
    return new_csv

sudan_csv = import_csv('ACLED_South-Sudan_2017.csv')


# Exercise 2 a)

import string

def normalise_text():
    """converts text into lower case and removes punctuation"""
    sudan_csv = import_csv('ACLED_South-Sudan_2017.csv')
    for line in sudan_csv[1:]:
        notes_low = line[-4].lower() # converts 'notes' to lower case
        table = str.maketrans(dict.fromkeys(string.punctuation)) # two lines that remove punctuation
        notes_low_normal = notes_low.translate(table)
        line[-4] = notes_low_normal # replace original 'notes' with the new normalised strings

    return sudan_csv

sudan_normalised = normalise_text()
# Test
print('sudan_normalised: ', sudan_normalised[1][-4])
print('\n')


# Exercise 2 c) Tokenising text before removing stopwords

def tokenise_text():
    """function that takes normalised text and turns each words into list element"""
    sudan_normalised = normalise_text()
    for row in sudan_normalised[1:]:
        split_notes = row[-4].split()
        row.append(split_notes)
    return sudan_normalised

sudan_tokenised = tokenise_text()
print('notes: ', sudan_tokenised[1][-5]) # the second index changes due to extra column
print('tokenised notes: ', sudan_tokenised[1][-1])
print('\n')

# if the tokensise_text() is ran an extra column is added and alters later functions

# Exercise 2b) removal of stopwords

stop_list = open('eng_stop_words.txt')
stop_list = stop_list.read()
stop_list = stop_list.split()


def remove_stopwords():
    """function that removes the stopwords from the new column of words"""
    sudan_tokenised = tokenise_text()
    for row in sudan_tokenised[1:]:
        thin_list = [word for word in row[-1] if word not in stop_list]
        row[-1] = thin_list

    return sudan_tokenised

sudan_filtered = remove_stopwords()
print('stopwords removed: ', sudan_filtered[1][-1])
print('\n')


# 3 a) insert

remove_stopwords() # Only function that is required as incorporates all previous functions


# Exercise 3 b)

import re

def extract_uncertain(): #Add function strings
    """function that extracts records that where the word 'reportedly' appears in notes"""
    sudan_processed = remove_stopwords()
    return [row for row in sudan_processed if bool(re.search("reportedly", row[-5]))]

uncertain_extract = extract_uncertain()

# Test
print('uncertain records: ', uncertain_extract[1][-1])
print('\n')


# # Exercise 3 c)

def extract_ambush():
    """function that extracts records where the word ambush in all it's conjugations is in the notes"""
    sudan_processed = remove_stopwords()
    return [row for row in sudan_processed if bool(re.search("ambush.*", row[-5]))]

# Test
ambush_extract = extract_ambush()
print('ambush records: ', ambush_extract[1][-1])

# Exercise 3 d)

import itertools
from collections import Counter

uncertain_words = [row[-1] for row in uncertain_extract] # Taking the words from extracted records
uncertain_words = list(itertools.chain.from_iterable(uncertain_words)) # Merging lists
print('\n')
print('10 most common words in uncertain set: ', Counter(uncertain_words).most_common(10))

ambush_words = [row[-1] for row in ambush_extract] # Taking the words from extracted records
ambush_words = list(itertools.chain.from_iterable(ambush_words)) # Merging lists
print('10 most common words in ambush set: ', Counter(ambush_words).most_common(10))


# A lot of the uncertain events seem to involve the government and the SPLAIO. The most common words in the records
# involving ambushes does not include 'reportedly' so they could be considered more certain.


