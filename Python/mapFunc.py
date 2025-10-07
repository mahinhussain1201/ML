# the map() function applies a function to each item in an iterable (like list, tuple) and returns an iterator.
def square(x):
    return x * x

nums = [1, 2, 3, 4]
squares = map(square, nums)
print(list(squares))
