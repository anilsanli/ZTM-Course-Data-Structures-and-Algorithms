numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(array):
    length = len(array)
    for i in range(length):
        for j in range(length-1):
            if array[j] > array[j+1]:
                # Swap the numbers
                array[j], array[j+1] = array[j+1], array[j]

bubbleSort(numbers)
print(numbers)
