# List comprehension is a shorter and often more “Pythonic” way to do what map() and filter() do.
nums = [1, 2, 3, 4]
squares = [x**2 for x in nums]
print(squares)  # [1, 4, 9, 16]
