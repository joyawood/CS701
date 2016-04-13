#word_counter.py
#CS 701
# Final project
'''
A function that given a text file returns the ten most
frequently used words and their ascociated frequencies.
'''
import re
from sys import argv
import operator
def word_counter():
    input_file = raw_input("> ") # get text file from user
    with open(input_file, 'r') as myfile: #convert to string
        data=myfile.read().replace('\n', ' ')

    x = data.lower()
    words = re.findall(r"[\w']+",x) # Remove punctuation marks and create a list of words
    d = {} # A dictionary for storing each word
    result = [] # An array for storing the final solutions
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    sorted_d = sorted(d.items(), key=operator.itemgetter(1))
    sorted_d.reverse()
    for i in range(20): #get the 20 most apearing words
        result.append(sorted_d[i])
    return result

print (word_counter())

# sample usage
# python word_counter.py
# >file_name.txt
