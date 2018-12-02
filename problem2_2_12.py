# Advent of Code - 2018
# Problem 2 of 2.12.2018
#
# In this task we need to find two strings from input file which have the most letters in common
#   (same index = same letter). Then we need to create a new word from these letters.

def compare(string1, string2):
    score = 0
    newword = ""

    for num in range(0, len(string1)):
        if string1[num] == string2[num]:
            score += 1
            newword += string1[num]

    return (newword, score)


file = open("Data/2_12.txt", "r")
array = []
final_word = ""
max_score = 0

for string in file.read().split():
    array.append(string)

for x in range(0, len(array)):
    for y in range (x+1, len(array)):
        (new_word, score) = compare(array[x], array[y])
        if score > max_score :
            final_word = new_word
            max_score = score

print(final_word)


