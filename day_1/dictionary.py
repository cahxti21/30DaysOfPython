"""
Python reads a dictionary by looking up unique keys using an underlying hash table structure to retrieve values instantly,
or by iterating through its keys and values using loops.
"""

# Reading a Single Value by Key
# The most direct way to read a value is to reference its key inside square brackets

user = {"name": "Alice", "age": 25}                              # A dictionary always pairs a Key to a Value using a ":"
                                                                 # Not to be confused with a set
# Read using square brackets
print(user["name"])                                              # Outputs: Alice
print(user["age"])                                               # Outputs: 25

# Note: If the key does not exist, square brackets will crash your program with a KeyError

# Reading Safely with .get()
# To prevent crashes from missing keys, use .get() method. It returns None or a custom default value if key isn't found.

print(user.get("email"))                                        # Outputs: None
print(user.get("email", "No email provided"))       # Outputs: No email provided

# Reading all items with a Loop
# You can read through a dictionary systematically using a for loop combined with built-in dictionary methods.

# Reads Keys only (Default behavior)
for key in user:
    print(key)
# Outputs: name
#          age

# Read Values only using .values()
for value in user.values():
    print(value)
# Outputs: Alice
#          25

# Read Both Keys and Values using .items() with tuple unpacking:
for key, value in user.items():
    print(f"{key}: {value}")
# Outputs: name: Alice
#          age: 25