def reverseString(str):
    arrayStr = list(str)
    reversedArray = []

    def addToArray(array):
        if len(array) > 0:
            reversedArray.append(array.pop())
            addToArray(array)

    addToArray(arrayStr)
    return ''.join(reversedArray)

reverseString("yoyo master")

def reverseStringRecursive(str):
    if str == "":
        return ""
    else:
        return reverseStringRecursive(str[1:]) + str[0]

reverseStringRecursive("yoyo master")
