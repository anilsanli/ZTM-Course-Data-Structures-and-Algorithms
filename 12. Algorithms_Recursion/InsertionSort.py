numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def insertionSort(array):
    length = len(array)

    for i in range(length):
        if array[i] < array[0]:
            # Move number to the first position
            array.insert(0, array.pop(i))
        else:
            # Find where number should go
            for j in range(1, i):
                if array[i] > array[j - 1] and array[i] < array[j]:
                    # Move number to the right spot
                    array.insert(j, array.pop(i))
                    break

    return array

print(insertionSort(numbers))
