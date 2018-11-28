"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

import random

def quicksort(array):

    if array == []:
        return array

    compare_index = 0
    p_index = len(array) - 1
    pivot = array[p_index]

    #Partition part
    while True:
        if compare_index == p_index:
            break
        if array[compare_index] >= pivot:
            tmp = array[compare_index]
            array[compare_index] = array[p_index - 1]
            array[p_index - 1] = pivot
            array[p_index] = tmp
            p_index -= 1
        else:
            compare_index += 1
            continue

    left_array = array[:p_index]
    left_array = quicksort(left_array)
    left_array.append(array[p_index])

    right_array = array[p_index + 1:]
    right_array = quicksort(right_array)

    return left_array + right_array


def quicksort_indexes(array, start_range, stop_range):

    compare_index = start_range
    p_index = stop_range
    pivot = array[p_index]

    #Partition part
    while True:
        if compare_index == p_index:
            break
        if array[compare_index] >= pivot:
            tmp = array[compare_index]
            array[compare_index] = array[p_index - 1]
            array[p_index - 1] = pivot
            array[p_index] = tmp
            p_index -= 1
        else:
            compare_index += 1
            continue

    #left part
    quicksort_indexes(array, 0, p_index - 1)

    #right part
    quicksort_indexes(array, p_index + 1, len(array) - 1)

    return array

test = []

for u in range(20):
    test.append(random.randint(0, 1000))

print(test)
print(sorted(test))

#print(quicksort(test))
ar = quicksort_indexes(test, 0, len(test) - 1)