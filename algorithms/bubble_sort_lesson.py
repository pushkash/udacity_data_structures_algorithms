import random


array = []

for x in range(20):
    array.append(random.randint(0, 200))

print(array)



def bubble_sort(array):

    index = 0
    end = len(array) - 1

    while end > 0:
        if index == end:
            index = 0
            end -= 1
        elif array[index] > array[index + 1]:
           tmp = array[index]
           array[index] = array[index + 1]
           array[index + 1] = tmp
           index += 1
        elif array[index] <= array[index + 1]:
            index += 1

print(sorted(array))
bubble_sort(array)

print(array)



