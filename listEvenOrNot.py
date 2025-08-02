import array as arr

my_array = arr.array('i', [10, 20, 30, 40, 50])

index = 0

array_length = len(my_array)

while index < array_length:
    print(my_array[index])
    index += 1
#my_array.append(60)
#print(my_array)