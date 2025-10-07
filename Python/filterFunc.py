# filter() function in Python is used to filter elements of an iterable based on a condition.
# It keeps only those elements for which the function returns True.
def is_even(x):
    return x % 2 == 0

nums = [1, 2, 3, 4, 5, 6]
evens = filter(is_even, nums)
print(list(evens))  # [2, 4, 6]
