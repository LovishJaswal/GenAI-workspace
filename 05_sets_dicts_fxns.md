# Day 05 – Sets, Dictionaries & Functions

## Training

**Course:** Python + Generative AI

**Day:** 05

---

# Topics Covered

- Tuples (Additional Concepts)
- Sets
- Set Methods
- Dictionary
- Dictionary Methods
- Functions
- Return Statement

---

# Tuples (Additional Concepts)

A tuple is an **ordered and immutable** collection of elements.

One common misconception is that parentheses `()` create a tuple. In reality, **the comma creates the tuple**, while parentheses improve readability.

### Example

```python
a = 10,
print(type(a))
```

Output

```text
<class 'tuple'>
```

The following are equivalent:

```python
a = 1, 2, 3
```

```python
a = (1, 2, 3)
```

Both create a tuple.

---

# Empty Tuple

An empty tuple can be created as:

```python
empty_tuple = ()
```

### Uses of an Empty Tuple

- Returning an empty immutable object.
- Default values in functions.
- Placeholder values.
- Constant data that should never change.

---

# Sets

A **set** is an unordered collection of unique elements.

Unlike lists and tuples, sets:

- Store only unique values.
- Do not support indexing.
- Are mutable.
- Automatically remove duplicate elements.

### Example

```python
numbers = {1, 2, 3, 4, 5}

print(numbers)
```

---

# Creating a Set

```python
a = {1, 2, 3}
```

Creating an empty set:

```python
a = set()
```

> **Important**
>
> `{}` creates an empty **dictionary**, not a set.

---

# Properties of Sets

- Unordered
- Mutable
- No duplicate values
- Cannot be indexed
- Cannot contain mutable objects like lists or other sets

Valid examples:

```python
{1, 2, 3}
```

```python
{"Python", "AI", "ML"}
```

Invalid example:

```python
{[1, 2, 3]}
```

Lists are mutable, so they cannot be stored inside a set.

---

# Why Can't We Modify a Set Using Indexing?

This is **incorrect**:

```python
a = {1, 2, 3}

a = list(a)
a[0] = 10
a = set(a)
```

Although this works, it is **not the intended way** to modify a set.

Since sets are unordered, elements have no fixed position.

Instead, use built-in set methods such as:

- `add()`
- `remove()`
- `discard()`
- `update()`

---

# Common Set Methods

### add()

Adds a new element.

```python
a = {1, 2, 3}

a.add(4)

print(a)
```

---

### remove()

Removes an element.

```python
a.remove(2)
```

Raises an error if the element does not exist.

---

### discard()

Removes an element without raising an error.

```python
a.discard(10)
```

---

### clear()

Removes every element from the set.

```python
a.clear()
```

Output:

```python
set()
```

---

### __contains__()

Checks whether an element exists.

```python
a = {1, 2, 3}

print(a.__contains__(2))
```

A more Pythonic approach is:

```python
print(2 in a)
```

---

# Set Operations

### Union

Returns every unique element from both sets.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
```

Output

```text
{1, 2, 3, 4, 5}
```

---

### Intersection

Returns only the common elements.

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))
```

Output

```text
{2, 3}
```

---

# Dictionaries

A **dictionary** is a mutable collection of **key-value pairs**.

Each key is unique and maps to a corresponding value.

### Syntax

```python
dictionary = {
    key: value
}
```

### Example

```python
student = {
    "name": "Alice",
    "age": 20,
    "city": "New York"
}
```

---

# Properties of Dictionaries

- Mutable
- Ordered (Python 3.7+)
- Keys must be unique.
- Values can be duplicated.
- Fast lookup using keys.

---

# Dictionary Keys

Dictionary keys must be **immutable (hashable)**.

Valid key types:

- `str`
- `int`
- `float`
- `bool`
- `tuple` (if it contains immutable elements)

Invalid key types:

- `list`
- `set`
- `dict`

### Valid Example

```python
student = {
    "name": "Alice",
    1: "Python",
    (10, 20): "Coordinates"
}
```

### Invalid Example

```python
data = {
    [1, 2]: "List"
}
```

This raises a **TypeError** because lists are mutable.

---

# Creating a Dictionary

```python
student = {
    "name": "Alice",
    "city": "New York",
    "age": 20
}
```

You can also create an empty dictionary.

```python
student = {}
```

or

```python
student = dict()
```

---

# Accessing Dictionary Values

### Using Square Brackets

```python
print(student["name"])
```

If the key does not exist, Python raises a `KeyError`.

---

### Using `get()`

```python
print(student.get("name"))
```

Using `get()` is safer because it returns `None` (or a default value) instead of raising an error.

```python
print(student.get("phone", "Not Available"))
```

---

# Adding New Elements

```python
student["course"] = "Python"
```

Output

```python
{
    "name": "Alice",
    "city": "New York",
    "age": 20,
    "course": "Python"
}
```

---

# Updating Existing Values

```python
student["age"] = 21
```

---

# Iterating Through a Dictionary

When iterating directly over a dictionary:

```python
for value in student:
    print(value)
```

The output contains **keys**, not values.

To access the corresponding values:

```python
for key in student:
    print(student[key])
```

A cleaner approach is:

```python
for key, value in student.items():
    print(key, value)
```

---

# Common Dictionary Methods

### `keys()`

Returns all keys.

```python
print(student.keys())
```

---

### `values()`

Returns all values.

```python
print(student.values())
```

---

### `items()`

Returns key-value pairs as tuples.

```python
print(student.items())
```

---

### `pop()`

Removes a specific key and returns its value.

```python
student.pop("age")
```

---

### `popitem()`

Removes and returns the **last inserted** key-value pair.

```python
student.popitem()
```

---

### `clear()`

Removes every element.

```python
student.clear()
```

---

### `update()`

Updates one dictionary using another dictionary.

```python
student.update({
    "country": "India",
    "language": "Python"
})
```

---

# Why Must Dictionary Keys Be Immutable?

Python internally uses a **hash value** to quickly locate dictionary keys.

Mutable objects (like lists and dictionaries) can change after being created, which would change their hash and make lookups unreliable.

For this reason, dictionary keys must be immutable.

---

# Additional Notes

- Dictionary values can be of any data type.
- Keys must always be unique.
- If the same key is used twice, the last value overwrites the previous one.

Example:

```python
student = {
    "name": "Alice",
    "name": "Bob"
}

print(student)
```

Output

```text
{'name': 'Bob'}
```

---

# Functions

A **function** is a reusable block of code designed to perform a specific task.

Functions help make programs:

- Modular
- Reusable
- Easier to read
- Easier to debug and maintain

---

# Why Use Functions?

Without functions, the same code may need to be written multiple times.

Functions allow us to write the logic once and reuse it whenever required.

---

# Function Syntax

```python
def function_name(parameters):
    # Function body
    return value
```

### Example

```python
def greet():
    print("Hello, World!")

greet()
```

---

# Function with Parameters

Functions can accept values called **parameters**.

```python
def add(a, b):
    return a + b

print(add(5, 10))
```

Output

```text
15
```

---

# Function Without Parameters

```python
def display():
    print("Welcome to Python")

display()
```

---

# Example from Class

```python
def fun():
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))

    return a + b

print(fun())
```

---

# The `return` Statement

The `return` keyword sends a value back to the caller.

```python
def square(number):
    return number * number

result = square(5)

print(result)
```

Output

```text
25
```

---

# What Happens If We Don't Return Anything?

If a function does not explicitly return a value, Python automatically returns **`None`**.

Example

```python
def greet():
    print("Hello")

result = greet()

print(result)
```

Output

```text
Hello
None
```

---

# Local Variables

Variables created inside a function are called **local variables**.

They exist only while the function is executing.

```python
def test():
    x = 10
    print(x)

test()
```

Trying to access `x` outside the function results in an error.

---

# Benefits of Functions

- Avoids code duplication.
- Improves readability.
- Makes debugging easier.
- Promotes code reusability.
- Makes programs easier to maintain.

---

# Common Mistakes

### Forgetting to Call the Function

```python
def greet():
    print("Hello")
```

Nothing happens until the function is called.

```python
greet()
```

---

### Forgetting the `return` Statement

```python
def add(a, b):
    a + b
```

Output

```python
print(add(2, 3))
```

```text
None
```

Correct version:

```python
def add(a, b):
    return a + b
```

---

### Confusing `print()` with `return`

```python
def add(a, b):
    print(a + b)
```

prints the result but returns `None`.

```python
def add(a, b):
    return a + b
```

returns the result so it can be stored or reused.

---

# Key Takeaways

- A tuple is created by the **comma**, while parentheses improve readability.
- Sets store **unique, unordered** elements.
- Sets are mutable but do not support indexing.
- Dictionaries store data as **key-value pairs**.
- Dictionary keys must be immutable.
- `get()` safely retrieves values without raising a `KeyError`.
- `keys()`, `values()`, and `items()` are commonly used dictionary methods.
- Functions improve code organization and reusability.
- Every Python function returns a value. If no value is specified, Python returns `None`.

---

# Homework

- Practice all common **set methods**.
- Explore dictionary methods using:

```python
help(dict)
```

- Create a dictionary to store student information.
- Write functions to perform:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Practice writing functions with and without parameters.
- Read about **positional arguments** and **keyword arguments**.
- Explore the difference between **local** and **global** variables.

---

> **End of Day 05**