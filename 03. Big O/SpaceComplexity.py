# #5 Space complexity O(1)
def boooo(n):
    for i in range(n):
        print("booooo")

# #6 Space complexity O(n)
def array_of_hi_n_times(n):
    hi_array = []
    for i in range(n):
        hi_array.append("hi")
    return hi_array

array_of_hi_n_times(6)
