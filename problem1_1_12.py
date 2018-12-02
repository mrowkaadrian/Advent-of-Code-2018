# Advent of Code - 2018
# Problem 1 of 1.12.2018
#
# We need to calculate last existing frequency our device will reach. We are using a .txt file, which contains
#   a number (positive or negative) in every single line. To calculate this, we need to add or subtract number of
#   each line, starting from value: 0

file = open("Data/1_12.txt", "r")

array = []
final_freq = 0

for val in file.read().split():
    array.append(int(val))
file.close()

for val in array:
    final_freq += val

print(final_freq)