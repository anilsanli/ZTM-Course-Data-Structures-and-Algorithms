numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def selectionSort(array):
    length = len(array)

    for i in range(length - 1):
        # Set current index as minimum
        min_index = i
        temp = array[i]

        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                # Update minimum if current is lower that what we had previously
                min_index = j

        array[i] = array[min_index]
        array[min_index] = temp

    return array

print(selectionSort(numbers))
