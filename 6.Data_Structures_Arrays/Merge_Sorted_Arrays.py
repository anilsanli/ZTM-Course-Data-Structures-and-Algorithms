def merge_sorted_arrays(array1, array2):
    merged_array = []
    array1_item = array1[0] if array1 else None
    array2_item = array2[0] if array2 else None
    i = 1
    j = 1

    # Checks for empty arrays
    if not array1_item:
        return array2
    if not array2_item:
        return array1

    while array1_item or array2_item:
        if array2_item is None or (array1_item is not None and array1_item < array2_item):
            merged_array.append(array1_item)
            if i < len(array1):
                array1_item = array1[i]
                i += 1
            else:
                array1_item = None
        else:
            merged_array.append(array2_item)
            if j < len(array2):
                array2_item = array2[j]
                j += 1
            else:
                array2_item = None

    return merged_array

# Test
print(merge_sorted_arrays([0,3,4,31], [3,4,6,30]))
