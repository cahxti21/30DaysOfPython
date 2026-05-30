my_list = [1, 2, 3] # define the list
print(id(my_list))  # Example output: [1, 2, 3]

# Modify an element in place
my_list[0] = 99     # Python uses zero-based indexing, meaning the very first item is located at index 0
print(id(my_list))  # Example output: [99, 2, 3]
print(my_list)      # Output: [99, 2, 3]
print(id(my_list))  # Output: 140237424 (The ID has NOT changed)
