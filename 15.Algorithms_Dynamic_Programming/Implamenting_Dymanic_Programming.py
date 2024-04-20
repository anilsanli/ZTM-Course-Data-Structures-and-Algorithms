# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233...
calculations = 0

def fibonacci(n):
    # O(2^n)
    global calculations
    calculations += 1
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_master():
    # O(n)
    cache = {}
    def fib(n):
        global calculations
        calculations += 1
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fib(n - 1) + fib(n - 2)
                return cache[n]
    return fib

def fibonacci_master2(n):
    answer = [0, 1]
    for i in range(2, n + 1):
        answer.append(answer[i - 2] + answer[i - 1])
    return answer[-1]

faster_fib = fibonacci_master()

print("Slow:", fibonacci(35))
print("DP:", faster_fib(100))
print("DP2:", fibonacci_master2(100))
print("we did", calculations, "calculations")
