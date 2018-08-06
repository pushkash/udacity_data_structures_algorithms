"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
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


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))