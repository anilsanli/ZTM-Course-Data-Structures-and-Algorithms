def print_all_numbers_then_all_pair_sums(numbers):
    print("these are the numbers:")
    for number in numbers:
        print(number)

    print("and these are their sums:")
    for first_number in numbers:
        for second_number in numbers:
            print(first_number + second_number)

print_all_numbers_then_all_pair_sums([1, 2, 3, 4, 5])  # O(n^2)
