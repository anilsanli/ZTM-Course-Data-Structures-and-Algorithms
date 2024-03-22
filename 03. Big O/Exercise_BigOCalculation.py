def funChallenge(input):
    a = 10 # O(1)
    a = 50 + 3 # O(1)

    for i in range(len(input)): # O(n)
        anotherFunction() # O(n)
        stranger = True # O(n)
        a += 1 # O(n)

    return a # O(1)

# 3 + n + n + n + n --> 3 + 4n --> BigO(3 + 4n) --> BigO(n)