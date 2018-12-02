# Advent of Code - 2018
# Problem 2 of 1.12.2018
#
# We need to detect first frequency our device reaches twice. We are using the same data as in the previous
#   task.

file = open("Data/1_12.txt", "r")

array = []
search_array = []
current_freq = 0
FOUND = 0

for val in file.read().split():
    array.append(int(val))
file.close()

while FOUND == 0:
    for val in array:
        current_freq += val
        if (current_freq in search_array):
            FOUND = 1
            print(current_freq)
            break
        else:
            search_array.append(current_freq)

print(current_freq)
