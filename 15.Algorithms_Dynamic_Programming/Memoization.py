def add_to_80(n):
    return n + 80

add_to_80(5)

def memoize_add_to_80():
    cache = {}
    def memoized(n):
        if n in cache:
            return cache[n]
        else:
            print('long time')
            answer = n + 80
            cache[n] = answer
            return answer
    return memoized

memoized = memoize_add_to_80()
print(1, memoized(6))
print(2, memoized(6))