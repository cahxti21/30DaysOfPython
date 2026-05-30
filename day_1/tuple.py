""" Python reads or accesses data from a tuple through indexing, slicing, loops, or unpacking.

Tuples are ordered and immutable (unchangeable/unmodifiable) collections, Python uses standard sequence operations to retrieve their values

"""

"""
Bracket indexing
"""
# Bracket indexing - Python maps each item to a specific index number starting at 0.
# You pass the index inside square brackets [] tp read a specific item.

# Positive indexing - reads from left to right, starting at 0.
user_data = ("Alice", 28, "Engineer")       # define the tuple using "("
print(user_data[0])                         # Outputs: Alice (First item)

# Negative indexing - reads from right to left, starting at -1
print(user_data[-1])                        # Outputs: Engineer (Last item)

"""
Slicing
"""
# Slicing (Reading Ranges of Items) - You can read a chunk/sub section of a tuple using ":" inside square brackets.
# The syntax follows tuple[start:stop:step]. The stop index is exclusive.

numbers = (10, 20, 30, 40, 50)              # define the tuple using "("

# Reads from index 1 up to (but not including) index 4
print(numbers[1:4])  # Outputs: (20, 30, 40)

# Reads every second item
print(numbers[::2])  # Outputs: (10, 30, 50)

"""
Tuples Unpacking - Reading all items simultaneously
"""

# Python allows you to read and assign all components of a tuple into individual variables in a single line of code

# Basic unpacking - The number of variables must match the number of tuple elements
coordinates = (4.5, -1.2, 9.8)              # define the tuple using "("

# Basic Unpacking
x, y, z = coordinates
print(x)                                    # Outputs: 4.5

# Asterisk Unpacking - Collects remaining unassigned items into a list if variable counts do not match
first, *rest = coordinates
print(rest)                                 # Outputs: -1.2, 9.8

# Basic unpacking and Asterisk Unpacking work Hand in hand.

letters = ('A', 'B', 'C', 'D', 'E')

# 'start' gets 'A', 'end' gets 'E' (Basic unpacking)
# '*middle' traps whatever is left in between
start, *middle, end = letters

print(start)   # 'A'
print(middle)  # ['B', 'C', 'D']
print(end)     # 'E'

"""
For Loops - Reading elements sequentially
"""

# To read through the entire dataset one item at a time, you can iterate through the tuple directly using a for loop

fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(fruit)

# Reading and Unpacking inside a for loop
shopping_cart = [
    ("Apples", 5, 0.99),
    ("Milk", 2, 2.50),
    ("Bread", 1, 3.10)
]
# tuple inside a list.

# The loop unpacks each tuple directly into three clean variables
for name, quantity, price in shopping_cart:
    total = quantity * price
    print(f"{quantity}x {name} costs ${total:.2f}")

# Step by step breakdown:
'''
When the for loop runs the first time, it grabs the first tuple ("Apples", 5, 0.99).

Then it does a basic assignment matching the positions

Position 0: name (Apple)
Position 1: quantity (5)
Position 2: price (0.99)
'''