# Strings

# Any Data wrapped inside im sings '...', double "...", or triple '''..'''/"""...""" quotes.
# Every SINGLE Character counts as a string.

letter = 'P'
greeting = "Hello, world!"
sentence = "Day 4 of 30 Days of Python Programming! So far So Good!)"
print(len(greeting))        #13
print(len(sentence))        #56

# len() returns the number of characters INCLUDING SPACES.

# Multiline strings
# Use triple quotes when your string spans multiple lines.

multiline = '''Line one.
Line two.
Line three.'''
print(multiline)

# String concatenation
# Join strings together with '+'. You can also check lengths and compare them.

first_name = "gian"
last_name = "daniel"
full_name = first_name + " " + last_name
print(full_name)
print(len(first_name) > len(last_name))

# Escape sequences
"""
| Escape | Meaning      |
| ------ | ------------ |
| `\n`   | New line     |
| `\t`   | Tab          |
| `\\`   | Backslash    |
| `\'`   | Single quote |
| `\"`   | Double quote |
"""
print('gian\n23\nSingapore')
print('testing\t23\"Singapore')

# String formatting - f-strings (preferred): the modern standard
a, b = 4, 3                         # Multiple variable assignment
print(f'{a} + {b} = {a + b}')       # Math and Text Mixing

print(f'Result: {a / b:.2f}')