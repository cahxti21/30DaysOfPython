# Assignment Operators
x = 5       # '=' assigns a value, x = 5
x += 3      # Adds amd assigns, x = x + 3
x -= 3      # Subtracts and assigns, x = x - 3
x *= 3      # Multiplies and assigns, x = x * 3
x /= 3      # Divides and assigns, x = x / 3

# Arithmetic Operators
# Practical Math Examples

a, b = 3, 2
print('Addition:', a + b)           # 5
print('Floor division:', a // b)    # 1 (Chops off the decimal)
print('Exponentiation:', a ** b)    # 9 (3 to the power of 2)
print('Complex Numbers:', 1 + 1j)   # Python supports complex math natively

# Comparison Operators
# Compares two values and always results in a Boolean ( True or False )
'''
| **Operator** | **Name**              | **Example** | **Result** |
| ------------ | --------------------- | ----------- | ---------- |
| `==`         | Equal to              | `3 == 2`    | `False`    |
| `!=`         | Not equal to          | `3 != 2`    | `True`     |
| `>`          | Greater than          | `3 > 2`     | `True`     |
| `<`          | Less than             | `2 < 3`     | `True`     |
| `>=`         | Greater than or equal | `3 >= 3`    | `True`     |
| `<=`         | Less than or equal    | `3 <= 2`    | `False`    |
'''
# You can even compare the lengths of strings
print(len('mango') == len('avocado'))  # False (5 == 7)
print(len('python') > len('dragon'))   # False (6 > 6)

# Logical Operators
'''
| **Operator** | **Description**                           | **Example**           | **Result** |
| ------------ | ----------------------------------------- | --------------------- | ---------- |
| `and`        | True if **both** statements are true      | `(3 > 2) and (4 > 3)` | `True`     |
| `or`         | True if **one** of the statements is true | `(3 > 2) or (4 < 3)`  | `True`     |
| `not`        | Reverses the result (True becomes False)  | `not (3 > 2)`         | `False`    |
'''

# Special Operators ( Identity & Membership )

# Identity - ( is, is not) Checks if two variables point to the exact same object in memory.
print('1 is 1:', 1 is 1)               # True
print('1 is not 2:', 1 is not 2)       # True

# Membership - ( in, not in ) Checks if a sequence (like a string or list) contains a specific item.
print('coding' in 'coding for all')    # True
print('B' not in 'Asabeneh')           # True (No uppercase B)