"""
# 🐍 Python Built-in Functions Cheat Sheet

## 🚀 Input / Output
- `print(...)` -> Displays data on the screen.
  ```python
  print("Hello, World!")
  ```
- `input(...)` -> Captures text typed by the user (always returns a string).
  ```python
  name = input("Enter your name: ")
  ```

## 🔍 Inspecting Data
- `type(...)` -> Identifies the data type.
  ```python
  type(42) # Returns: <class 'int'>
  ```
- `len(...)` -> Counts items in text, lists, or dictionaries.
  ```python
  len("Python") # Returns: 6
  ```

## 🔀 Type Conversion (Casting)
- `str(...)` -> Converts a value into text.
  ```python
  str(100) # Returns: '100'
  ```
- `int(...)` -> Converts text or decimals into a whole integer.
  ```python
  int("25") # Returns: 25
  ```
- `float(...)` -> Converts text or integers into a decimal.
  ```python
  float("9.99") # Returns: 9.99
  ```

## 🔢 Math Utilities
- `abs(...)` -> Strips the negative sign from a number.
  ```python
  abs(-5) # Returns: 5
  ```
- `round(...)` -> Rounds a decimal to the nearest whole number.
  ```python
  round(3.7) # Returns: 4
  ```
- `sum(...)` -> Adds up a collection of numbers.
  ```python
  sum([1, 2, 3]) # Returns: 6
  ```
- `min(...)` / `max(...)` -> Finds the lowest or highest value.
  ```python
  max(5, 12, 3) # Returns: 12
  ```

## 🛠️ Loops & Sequences
- `range(...)` -> Generates a sequence of numbers (great for loops).
  ```python
  range(5) # Generates: 0, 1, 2, 3, 4
  ```
- `sorted(...)` -> Returns a new, sorted version of a collection.
  ```python
  sorted([3, 1, 2]) # Returns: [1, 2, 3]
  ```

## 💡 Built-in Help
- `help(...)` -> Shows the official documentation inside your terminal.
  ```python
  help(print)
  ```
"""