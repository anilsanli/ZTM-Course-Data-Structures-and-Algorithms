def printFirstItemThenFirstHalfThenSayHi100Times(items):
    print(items[0]) # O(1)

    middleIndex = len(items) // 2
    index = 0

    while index < middleIndex:
        print(items[index]) # O(n/2)
        index += 1

    for i in range(100): # O(100)
        print('hi')

# 1 + n/2 + 100 --> O(n/2 + 101) --> O(n)