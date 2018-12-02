# Advent of Code - 2018
# Problem 1 of 2.12.2018
#
# In this task we need to calculate occurrences of each letter in every word in input file, then multiply *number
#   of words where any letter ocurred twice* with *number of words where any letter occured 3 times*

file = open("Data/2_12.txt", "r")

array = []
is_double = 0
is_triple = 0
doubles = 0
triples = 0

for val in file.read().split():
    array.append(val)

for string in array:
    for letter in string:
        count = string.count(letter)

        if count == 2:
            is_double = 1
        if count == 3:
            is_triple = 1
    if is_double == 1:
        doubles += 1
    if is_triple == 1:
        triples += 1

    is_double = 0
    is_triple = 0

print(doubles*triples)
