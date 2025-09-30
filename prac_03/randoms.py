import random

# Line 1
print(random.randint(5, 20))
# Produces a random integer between 5 and 20 inclusive.
# Smallest possible: 5
# Largest possible: 20

# Line 2
print(random.randrange(3, 10, 2))
# Produces a random integer from 3 up to (but not including) 10, stepping by 2.
# Possible values: 3, 5, 7, 9
# Smallest possible: 3
# Largest possible: 9
# Could line 2 have produced a 4? No, because step = 2 skips even numbers.

# Line 3
print(random.uniform(2.5, 5.5))
# Produces a random floating-point number between 2.5 and 5.5.
# Smallest possible: 2.5
# Largest possible: 5.5

# Extra task: random number between 1 and 100 inclusive
print(random.randint(1, 100))
