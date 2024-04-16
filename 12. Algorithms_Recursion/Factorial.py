def findFactorialIterative(number):
    answer = 1
    for i in range(2, number + 1):
        answer *= i
    return answer

def findFactorialRecursive(number):
    if number == 2:
        return 2
    return number * findFactorialRecursive(number - 1)

findFactorialIterative(5)
findFactorialRecursive(5)
