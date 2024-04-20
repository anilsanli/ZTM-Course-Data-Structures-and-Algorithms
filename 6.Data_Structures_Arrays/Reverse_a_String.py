def reverse(string):
    if not string or not isinstance(string, str) or len(string) < 2:
        return string

    backwards = []
    total_items = len(string) - 1
    for i in range(total_items, -1, -1):
        backwards.append(string[i])
    return ''.join(backwards)


def reverse2(string):
    # Check for valid input
    return ''.join(reversed(string))


def reverse3(string):
    # Check for valid input
    return ''.join(list(string)[::-1])


# Test
print(reverse('Timbits Hi'))  # Output: iH stibmiT
print(reverse2('Timbits Hi'))  # Output: iH stibmiT
print(reverse3('Timbits Hi'))  # Output: iH stibmiT
