# Mutable behavior - List, Set

"""
List
"""
# You can add, remove, or modify items directly inside a list

my_list = [1, 2, 3] # define the list using "["
print(id(my_list))  # Example output: [1, 2, 3]

# Modify an element in place
my_list[0] = 99     # Python uses zero-based indexing, meaning the very first item is located at index 0
print(id(my_list))  # Example output: [99, 2, 3]
print(my_list)      # Output: [99, 2, 3]
print(id(my_list))  # Output: 140237424 (The ID has NOT changed)


"""
Set
"""

# Is an unordered and unindexed collection.

my_set = {"apple", "banana", "cherry"}      # define the set using "{"

for item in my_set:
    print(item)                             # Example output:
"""                                           
cherry
apple
banana
""" # Due to the unordered nature of sets (unindexed), elements may be read in an unpredictable sequence

# You can check for specific elements in sets

my_set2 = {"apple", "banana", "cherry"}

# Returns True or False
is_present = "banana" in my_set2
print(is_present)

# How sets are mutable - You can modify a set by using built-in methods like: .add(), .remove(), .discard(), or .pop()

colors = {"red", "green", "blue"}
print(colors)  # Output: {'red', 'green', 'blue'}

# 2. Add an item (Shows Mutability)
colors.add("yellow")
print(colors)  # Output: {'red', 'green', 'yellow', 'blue'}

# 3. Remove an item (Shows Mutability)
colors.discard("green")
print(colors)  # Output: {'red', 'yellow', 'blue'}
