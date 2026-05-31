"""
# 📦 Python Variables Cheat Sheet

## 🔑 The Golden Rules
- **Assignment**: Variables are created using a single equals sign (`=`).
- **No Declaration**: You do not need to declare a type (like `int` or `string`) before creating a variable. Python figures it out automatically.
- **Dynamic**: You can change a variable's data type at any time.
  ```python
  x = 10     # x is an integer
  x = "Ten"  # Now x is a string
  ```

## 📛 Naming Rules (The "Can" and "Cannot")
- ✅ **Can** start with a letter or an underscore (`_`).
- ✅ **Can** contain numbers (just not at the start).
- ❌ **Cannot** start with a number (e.g., `1user` is invalid).
- ❌ **Cannot** contain spaces or symbols (e.g., `user-name` or `user$`).
- ❌ **Cannot** use Python **Reserved Keywords** (e.g., `print`, `if`, `for`, `class`).
- _if # if we want to use reserved word as a variable

## 💅 Styling Convention (PEP 8)
Python uses **snake_case** for variable names. Use lowercase letters and separate words with underscores.
```python
# Good practice
user_age = 25
first_name = "Alex"

# Bad practice
userAge = 25    # camelCase (used in JavaScript, avoid in Python)
UserAge = 25    # PascalCase (reserved for Python Classes)
```

## ⚡ Pro-Tricks (Multiple Variables)
You can declare multiple variables on a single line to keep your code clean.

### 1. Multiple assignments to different values
```python
name, age, is_learning = "Alex", 25, True
```

### 2. Same value to multiple variables
```python
score1 = score2 = score3 = 0
```

## ⚠️ Common Pitfalls
- **Case Sensitivity**: `age`, `Age`, and `AGE` are three completely different variables.
- **Overwriting Built-ins**: Never name a variable after a built-in function (e.g., `str = "Hello"`), or you will break that function for the rest of your script.

"""