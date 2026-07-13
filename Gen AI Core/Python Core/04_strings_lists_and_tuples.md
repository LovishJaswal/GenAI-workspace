# Day 04 – Strings, Lists & Tuples

## Training

**Course:** Python + Generative AI

**Day:** 04

---

# Topics Covered

- Strings
- String Methods
- String Slicing
- Lists
- List Comprehension
- Filtering Lists
- Tuples
- List vs Tuple

---

# Strings

A **string** is a sequence of characters enclosed within:

- Single quotes `' '`
- Double quotes `" "`
- Triple single quotes `''' '''`
- Triple double quotes `""" """`

A string can contain:

- Letters (`A-Z`, `a-z`)
- Numbers (`0-9`)
- Symbols (`@`, `#`, `$`, `%`, etc.)
- Spaces

### Example

```python
name = "Lovish"
language = 'Python'

message = """
Python supports
multi-line strings.
"""
```

> **Note**
>
> Strings are **immutable**, meaning they cannot be modified after creation.

---

# Common String Methods

Python provides several built-in methods for manipulating strings.

| Method | Description |
|---------|-------------|
| `capitalize()` | Converts the first character to uppercase. |
| `lower()` | Converts all characters to lowercase. |
| `upper()` | Converts all characters to uppercase. |
| `strip()` | Removes leading and trailing whitespace. |
| `split()` | Splits a string into a list. |
| `replace()` | Replaces one substring with another. |
| `find()` | Returns the index of the first occurrence of a substring. |
| `count()` | Counts the number of occurrences of a substring. |

### Example

```python
text = "  hello python  "

print(text.capitalize())
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("python", "world"))
```

> **Common Mistake**
>
> - `strip()` is the correct method, **not** `srip()`.
> - There is **no** string method named `list()`.

---

# String Slicing

Strings support both **indexing** and **slicing**.

### Syntax

```python
string[start : stop : step]
```

### Example

```python
name = "Python"

print(name[0])      # P
print(name[-1])     # n
print(name[0:4])    # Pyth
print(name[::2])    # Pto
print(name[::-1])   # nohtyP
```

> **Note**
>
> The **stop index is not included** in the output.

---

# Lists

A **list** is an ordered, mutable collection of elements enclosed within square brackets `[]`.

Lists can store:

- Integers
- Floating-point numbers
- Strings
- Objects
- Mixed data types

### Example

```python
numbers = [1, 2, 3, 4, 5]
```

Lists support:

- Indexing
- Slicing
- Adding elements
- Removing elements
- Updating existing values

### Accessing List Elements

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[-1])
```

---

# List Comprehension

List Comprehension provides a concise way to create a new list from an existing iterable.

### Syntax

```python
[expression for item in iterable]
```

### Example

```python
values = [1, 2, 3, 4, 5]

new_list = [x * 2 for x in values]

print(new_list)
```

### Output

```text
[2, 4, 6, 8, 10]
```

---

# Why Use List Comprehension?

Compared to a traditional `for` loop, List Comprehension:

- Requires fewer lines of code.
- Is easier to read for simple transformations.
- Is generally faster for creating new lists.

---

# Filtering Even Numbers

List Comprehension can also be used to filter elements based on a condition.

### Example

```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = [x for x in values if x % 2 == 0]

print(even_numbers)
```

### Output

```text
[2, 4, 6, 8]
```

---

# Filtering Odd Numbers

### Example

```python
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_numbers = [x for x in values if x % 2 != 0]

print(odd_numbers)
```

### Output

```text
[1, 3, 5, 7, 9]
```

---

# Tuples

A **tuple** is an ordered collection of elements enclosed within parentheses `()`.

Unlike lists, tuples are **immutable**, meaning their elements cannot be modified after creation.

Tuples can store multiple data types.

### Syntax

```python
tuple_name = (value1, value2, value3)
```

### Example

```python
student = ("Lovish", 20, "CSE")

print(student)
```

---

# Accessing Tuple Elements

Like lists, tuples support indexing and slicing.

```python
student = ("Lovish", 20, "CSE")

print(student[0])
print(student[-1])
```

---

# List vs Tuple

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Elements can be modified | Elements cannot be modified |
| Suitable for frequently changing data | Suitable for fixed data |
| Slightly slower | Slightly faster |

---

# When to Use Lists and Tuples

### Use a List when:

- Data needs to be modified.
- Elements need to be added or removed.
- Frequent updates are expected.

### Use a Tuple when:

- Data should remain constant.
- You want to prevent accidental modification.
- Storing fixed records such as coordinates or configuration values.

---

# Additional Notes

- Strings, like tuples, are immutable.
- Lists are one of the most commonly used data structures in Python because of their flexibility.
- List Comprehension always creates a **new list**; it does not modify the original list.
- Both lists and tuples support indexing and slicing.

---

# Key Takeaways

- Strings are immutable sequences of characters.
- Python provides many built-in string methods for text manipulation.
- String slicing follows the syntax:

```python
[start : stop : step]
```

- Lists are mutable collections.
- List Comprehension provides a concise way to create and filter lists.
- Tuples are immutable collections and are ideal for storing fixed data.
- Choosing between a list and a tuple depends on whether the data needs to change.

---

# Homework

- Practice string slicing with different values of `start`, `stop`, and `step`.
- Explore additional string methods using:

```python
help(str)
```

- Solve problems using List Comprehension.
- Compare the behavior of lists and tuples when attempting to modify their contents.
- Practice accessing elements using both positive and negative indexing.