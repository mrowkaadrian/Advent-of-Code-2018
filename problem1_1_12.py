file = open("problem1_1_12_DATA.txt", "r")

array = []
final_number = 0

for val in file.read().split():
    array.append(int(val))
file.close()

for val in array:
    final_number += val

print(final_number)