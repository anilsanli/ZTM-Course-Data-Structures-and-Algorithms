def fibonacciIterative(n):
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i - 2] + arr[i - 1])
    return arr[n]

fibonacciIterative(3)

def fibonacciRecursive(n):
    if n < 2:
        return n
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)

fibonacciRecursive(6)
