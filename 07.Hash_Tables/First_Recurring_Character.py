def first_recurring_character(input):
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[i] == input[j]:
                return input[i]
    return None

def first_recurring_character2(input):
    map = {}
    for i in range(len(input)):
        if input[i] in map:
            return input[i]
        else:
            map[input[i]] = i
    return None

first_recurring_character2([1,5,5,1,3,4,6])
first_recurring_character2([2,5,1,2,3,5,1,2,4])
first_recurring_character2([2,1,1,2,3,5,1,2,4])
first_recurring_character2([2,3,4,5])
