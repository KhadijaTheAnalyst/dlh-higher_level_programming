# Holberton/ALX Python Curriculum Cheat Sheet

## 1. PYTHON BASICS

### Print & Format Strings
```python
# Simple print
print("Hello World")

# Format with f-string
name = "John"
age = 25
print(f"Name: {name}, Age: {age}")

# Format with .format()
print("Name: {}, Age: {}".format(name, age))

# Old-style formatting
print("Name: %s, Age: %d" % (name, age))
```

### Variables & Data Types
```python
# String
name = "John"
text = 'Single or double quotes'

# Integer
age = 25
count = 0

# Float
price = 19.99
average = 3.14

# Boolean
is_student = True
is_active = False

# NoneType
value = None
```

### String Slicing & Operations
```python
text = "Hello"

# Slicing
text[0]      # 'H' (first character)
text[-1]     # 'o' (last character)
text[1:4]    # 'ell' (from index 1 to 3)
text[:3]     # 'Hel' (first 3 chars)
text[2:]     # 'llo' (from index 2 to end)

# String methods
text.upper()       # 'HELLO'
text.lower()       # 'hello'
text.replace("l", "L")  # 'HeLLo'
len(text)          # 5
```

### Input/Output
```python
# Get user input
name = input("Enter your name: ")

# Command line arguments
import sys
name = sys.argv[1]  # First argument
all_args = sys.argv  # List of all arguments
```

---

## 2. DATA STRUCTURES

### Lists (ordered, mutable)
```python
# Create list
my_list = [1, 2, 3, 4, 5]
my_list = []

# Access elements
my_list[0]      # First element: 1
my_list[-1]     # Last element: 5

# Add elements
my_list.append(6)       # Add to end
my_list.extend([7, 8])  # Add multiple
my_list.insert(0, 0)    # Insert at position

# Remove elements
my_list.remove(3)       # Remove by value
my_list.pop()           # Remove last
my_list.pop(0)          # Remove by index

# List operations
len(my_list)            # Length: 6
3 in my_list            # Check if exists
my_list.sort()          # Sort in place
my_list.reverse()       # Reverse in place
sorted(my_list)         # Returns sorted copy

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in my_list if x % 2 == 0]
```

### Tuples (ordered, immutable)
```python
# Create tuple
my_tuple = (1, 2, 3)
my_tuple = 1, 2, 3      # Parentheses optional

# Access (same as list)
my_tuple[0]             # 1
my_tuple[-1]            # 3

# Unpacking
a, b, c = my_tuple      # a=1, b=2, c=3

# Operations
len(my_tuple)           # 3
2 in my_tuple           # True
```

### Dictionaries (key-value pairs, mutable)
```python
# Create dictionary
my_dict = {"name": "John", "age": 25}
my_dict = {}

# Access elements
my_dict["name"]         # "John"
my_dict.get("name")     # "John" (safer)
my_dict.get("city", "Unknown")  # Default value

# Add/Update elements
my_dict["city"] = "New York"
my_dict.update({"country": "USA"})

# Remove elements
del my_dict["age"]
my_dict.pop("age")

# Dictionary operations
len(my_dict)            # Number of keys
"name" in my_dict       # Check if key exists
my_dict.keys()          # All keys
my_dict.values()        # All values
my_dict.items()         # Key-value pairs

# Loop through dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

### Sets (unordered, unique values)
```python
# Create set
my_set = {1, 2, 3, 4, 5}
my_set = set()

# Add elements
my_set.add(6)

# Remove elements
my_set.remove(3)        # Raises error if not found
my_set.discard(3)       # No error if not found

# Set operations
len(my_set)             # 5
3 in my_set             # Check if exists
my_set.union({4, 5, 6})         # {1, 2, 3, 4, 5, 6}
my_set.intersection({3, 4, 5})  # {3, 4, 5}
my_set.difference({4, 5, 6})    # {1, 2, 3}
```

---

## 3. CONTROL FLOW

### If/Elif/Else
```python
age = 25

if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"
```

### Loops
```python
# For loop
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for item in my_list:
    print(item)

for key, value in my_dict.items():
    print(f"{key}: {value}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
break       # Exit loop
continue    # Skip iteration
```

---

## 4. FUNCTIONS

### Function Definition
```python
# Simple function
def greet():
    print("Hello!")

# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

# Function with default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

# Function with return value
def add(a, b):
    return a + b

# Function with multiple return values
def get_info():
    return "John", 25, "NYC"
name, age, city = get_info()

# Function with *args (variable arguments)
def sum_all(*args):
    return sum(args)
sum_all(1, 2, 3, 4, 5)  # 15

# Function with **kwargs (keyword arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="John", age=25)
```

### Docstrings
```python
def add(a, b):
    """Add two numbers and return the result.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: The sum of a and b
    """
    return a + b
```

---

## 5. OBJECT-ORIENTED PROGRAMMING (OOP)

### Class Definition
```python
class Student:
    """A student class."""
    
    def __init__(self, name, age):
        """Initialize a Student instance."""
        self.name = name
        self.age = age

# Create instance
student = Student("John", 20)
print(student.name)  # "John"
```

### Special Methods (Dunder Methods)
```python
class Student:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        """Called by print() and str()"""
        return f"Student: {self.name}"
    
    def __repr__(self):
        """Called by repr() - should return valid Python code"""
        return f"Student('{self.name}')"
    
    def __len__(self):
        """Called by len()"""
        return len(self.name)
    
    def __del__(self):
        """Called when object is deleted"""
        print(f"{self.name} deleted")

# Usage
s = Student("John")
print(s)          # Calls __str__()
repr(s)           # Calls __repr__()
len(s)            # Calls __len__()
del s             # Calls __del__()
```

### Properties (Getters/Setters)
```python
class Square:
    def __init__(self, size):
        self.__size = size  # Private attribute
    
    @property
    def size(self):
        """Getter"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter with validation"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        return self.__size ** 2

# Usage
square = Square(5)
print(square.size)      # 5 (calls getter)
square.size = 10        # Calls setter with validation
print(square.area())    # 100
```

### Private Attributes
```python
class Person:
    def __init__(self, name):
        self.__name = name  # Private attribute (name mangling)
    
    def get_name(self):
        return self.__name

p = Person("John")
print(p.__name)         # ERROR! AttributeError
print(p._Person__name)  # Works but don't use this!
print(p.get_name())     # "John"
```

### Class Methods & Static Methods
```python
class Student:
    number_of_students = 0
    
    def __init__(self, name):
        self.name = name
        Student.number_of_students += 1
    
    @classmethod
    def get_total_students(cls):
        """Class method - takes cls instead of self"""
        return cls.number_of_students
    
    @staticmethod
    def is_adult(age):
        """Static method - no self or cls"""
        return age >= 18

# Usage
Student.get_total_students()  # 0
s1 = Student("John")
s2 = Student("Jane")
Student.get_total_students()  # 2
Student.is_adult(25)          # True
```

### Instance vs Class Attributes
```python
class Student:
    school = "Holberton"  # Class attribute (shared by all)
    
    def __init__(self, name):
        self.name = name  # Instance attribute (unique to each)

s1 = Student("John")
s2 = Student("Jane")

print(s1.name)      # "John"
print(s2.name)      # "Jane"
print(s1.school)    # "Holberton" (from class)
print(Student.school)  # "Holberton"
```

---

## 6. INHERITANCE

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

# Child class
class Dog(Animal):
    def speak(self):  # Override
        return f"{self.name} barks"

# Usage
dog = Dog("Buddy")
print(dog.speak())  # "Buddy barks"
```

---

## 7. TYPE CHECKING

```python
# isinstance() - check if object is instance of class
isinstance(student, Student)    # True
isinstance(5, int)              # True
isinstance(True, bool)          # True (bool is subclass of int!)

# type() - get exact type
type(5) == int                  # True
type(5) == bool                 # False

# Avoid using type() for type checking - use isinstance()
if isinstance(student, Student):  # ✅ Good
    pass

if type(student) == Student:      # ❌ Avoid
    pass
```

---

## 8. FILE I/O & SERIALIZATION

### File Operations
```python
import json
import csv
import pickle

# Read file
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Write file
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello World")

# Append to file
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("\nNew line")
```

### JSON
```python
import json

# Save dict to JSON
data = {"name": "John", "age": 25}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

# Load JSON to dict
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# String to dict
json_string = '{"name": "John"}'
data = json.loads(json_string)

# Dict to string
data = {"name": "John"}
json_string = json.dumps(data)
```

### CSV
```python
import csv

# Read CSV
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Write CSV
import csv
data = [{"name": "John", "age": 25}]
with open("data.csv", "w", encoding="utf-8") as f:
    fieldnames = ["name", "age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```

### Pickle
```python
import pickle

# Save object
obj = Student("John", 20)
with open("object.pkl", "wb") as f:
    pickle.dump(obj, f)

# Load object
with open("object.pkl", "rb") as f:
    obj = pickle.load(f)
```

---

## 9. COMMON PATTERNS

### Try-Except (Error Handling)
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Cleanup code")
```

### With Statement (Context Manager)
```python
# Automatically closes file
with open("file.txt", "r") as f:
    content = f.read()
# File is closed here
```

### List Comprehension
```python
# Simple
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# With transformation
upper_names = [name.upper() for name in ["john", "jane"]]  # ['JOHN', 'JANE']

# Nested
matrix = [[x*y for x in range(3)] for y in range(3)]
```

### Unpacking
```python
# Tuple unpacking
a, b, c = (1, 2, 3)

# Swap variables
a, b = b, a

# Multiple assignment
x = y = z = 0

# Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5
```

---

## 10. IMPORT STATEMENTS

```python
# Import entire module
import json
result = json.dumps(data)

# Import specific class/function
from csv import DictReader
reader = DictReader(file)

# Import with alias
import json as j
result = j.dumps(data)

# Import all (avoid in production)
from json import *

# Relative import (in packages)
from . import module_name
from ..utils import helper
```

---

## 11. SHEBANG & DOCSTRINGS

### Shebang (for executable scripts)
```python
#!/usr/bin/python3
```

### Module Docstring
```python
#!/usr/bin/python3
"""Module description - what this module does.

Additional details about the module.
"""

import sys
```

### Class Docstring
```python
class Student:
    """A student class with name and age."""
```

### Function Docstring
```python
def add(a, b):
    """Add two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: The sum of a and b
    """
    return a + b
```

---

## 12. COMMON ERRORS & SOLUTIONS

| Error | Cause | Solution |
|---|---|---|
| `IndexError` | List index out of range | Check list length before accessing |
| `KeyError` | Dict key doesn't exist | Use `.get()` or check with `in` |
| `TypeError` | Wrong data type | Use `isinstance()` to check type |
| `AttributeError` | Attribute doesn't exist | Check object has attribute |
| `FileNotFoundError` | File doesn't exist | Use try-except or check path |
| `NameError` | Variable not defined | Check variable name spelling |
| `ValueError` | Invalid value | Validate input before using |

---

## 13. BEST PRACTICES

✅ Always use `with` for file operations
✅ Add docstrings to modules, classes, and functions
✅ Use meaningful variable names
✅ Keep lines under 79 characters (PEP 8)
✅ Use `isinstance()` instead of `type()`
✅ Use properties for validation
✅ Handle exceptions appropriately
✅ Use `encoding="utf-8"` when opening files
✅ Add shebang (`#!/usr/bin/python3`) for executable scripts
✅ Private attributes with `__` prefix (name mangling)

---

## 14. USEFUL BUILT-IN FUNCTIONS

```python
len(x)              # Length
type(x)             # Data type
isinstance(x, type) # Type check
int(), str(), float(), list(), dict(), tuple(), set()  # Type conversion
range(start, stop, step)  # Range of numbers
enumerate(list)     # Index and value
zip(list1, list2)   # Combine lists
map(function, list) # Apply function
filter(function, list)  # Filter elements
sorted(list)        # Sort
sum(list)           # Sum
min(list), max(list)  # Min/max
all(list), any(list)  # All/any true
abs(x)              # Absolute value
round(x, decimals)  # Round number
hasattr(obj, "attr")  # Check attribute
getattr(obj, "attr")  # Get attribute
setattr(obj, "attr", value)  # Set attribute
```

---

## 15. QUICK REFERENCE TABLE

| Concept | Syntax | Example |
|---|---|---|
| **Variable** | `name = value` | `x = 5` |
| **Function** | `def func():` | `def add(a, b): return a+b` |
| **Class** | `class Name:` | `class Student: pass` |
| **Loop** | `for x in y:` | `for i in range(5): print(i)` |
| **Condition** | `if x: elif y: else:` | `if age >= 18: print("Adult")` |
| **List** | `[1, 2, 3]` | `my_list.append(4)` |
| **Dict** | `{"key": value}` | `my_dict["key"] = value` |
| **Tuple** | `(1, 2, 3)` | `a, b = (1, 2)` |
| **String** | `"text"` | `text[0:3]` |
| **Try** | `try: except:` | `try: x/0 except ZeroDivisionError:` |

---

## FINAL NOTES

- **Always test your code** before submitting
- **Use descriptive names** for variables and functions
- **Follow PEP 8** style guide
- **Comment complex logic**
- **Handle errors gracefully**
- **Never hardcode values** - use parameters and variables
- **Validate user input**
- **Use meaningful variable names, not a, b, c**

Good luck with Holberton/ALX! 🚀
