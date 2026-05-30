print(3 + 4)        # addition
print(3 - 4)         # subtraction
print(3 * 4)        # multiplication(*)
print(3 / 4)        # division
print(3 ** 4)       # exponential(**)
print(3 % 4)        # modulus(%)
print(3 // 4)       # floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(9.8))        # Float
print(type(3.14))       # Float
print(type(4 - 4j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List - are ordered, mutable collections that allow duplicates
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set - are unordered, mutable collections of completely unique elements
print(type((9.8, 3.14, 2.7)))    # Tuple - are ordered, immutable collections that allow duplicates

"""Mutable behavior - List, Set

You can add, remove, or modify items directly inside a list

e.g. - 
"""

my_list = [1, 2, 3] # define the list
print(id(my_list))  # Example output: [1, 2, 3]

# Modify an element in place
my_list[0] = 99     # Python uses zero-based indexing, meaning the very first item is located at index 0
print(id(my_list))  # Example output: [99, 2, 3]
print(my_list)      # Output: [99, 2, 3]
print(id(my_list))  # Output: 140237424 (The ID has NOT changed)
