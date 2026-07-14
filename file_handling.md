# File Handling

---

# Introduction

File handling allows a program to **create, read, write, append, and modify files** stored on a computer.

Python provides built-in functions to work with files efficiently.

---

# Types of Files

Files are generally divided into two categories:

## 1. Text Files

Text files store data in a human-readable format.

Examples:

- `.txt`
- `.csv`
- `.json`
- `.xml`

Example:

```text
Name=Lovish
Age=20
City=Hoshiarpur
```

---

## 2. Binary Files

Binary files store data in binary (0s and 1s) and are **not human-readable**.

Examples:

- `.jpg`
- `.png`
- `.mp4`
- `.pdf`
- `.exe`

Binary files must be opened using binary modes (`rb`, `wb`, etc.).

---

# Opening a File

Syntax:

```python
file = open("file.txt", "mode")
```

Example:

```python
file = open("file.txt", "r")
```

The `open()` function returns a file object that can be used for reading or writing.

---

# File Modes

| Mode | Description |
|------|-------------|
| `r` | Read a file (default mode). Raises an error if the file does not exist. |
| `w` | Write to a file. Creates a new file if it doesn't exist. If the file exists, all existing data is erased. |
| `a` | Append data to the end of a file without deleting existing content. |
| `rb` | Read a binary file. |
| `wb` | Write a binary file. Creates or overwrites the file. |

---

# Writing to a File

```python
file = open("file.txt", "w")

data = file.write("This is test")

file.close()

print(data)
```

`write()` returns the number of characters written.

---

# Reading a File

```python
file = open("file.txt", "r")

data = file.read()

file.close()

print(data)
```

`read()` reads the entire file.

---

# Append Mode

Append mode adds new data without deleting the existing content.

```python
file = open("file.txt", "a")

file.write("\nNew Line")

file.close()
```

---

# File Pointer

Whenever a file is opened, Python maintains a **file pointer (cursor)**.

The pointer keeps track of the current reading or writing position.

Example:

```python
file = open("file.txt", "r")

print(file.read(4))
print(file.read())
```

If the file contains

```text
Python Programming
```

Output:

```text
Pyth
on Programming
```

The second `read()` starts from where the first one stopped because both use the same file pointer.

---

# `readline()`

Reads one line at a time.

```python
with open("file.txt", "r") as file:

    print(file.readline())
    print(file.readline())
```

---

# `readlines()`

Reads all lines and returns them as a list.

```python
with open("file.txt", "r") as file:

    print(file.readlines())
```

Example output:

```python
['A=10\n', 'B=15\n', 'C=20\n']
```

---

# `read()`, `readline()` and `readlines()`

| Method | Returns |
|---------|----------|
| `read()` | Entire file as a string |
| `readline()` | One line at a time |
| `readlines()` | List containing every line |

All three methods use the **same file pointer**.

---

# Why Use `with open()`?

Using `open()` manually requires calling `close()`.

If an error occurs before `close()`, the file may remain open.

Instead, use a context manager.

```python
with open("file.txt", "r") as file:

    print(file.read())
```

Advantages:

- Automatically closes the file.
- Prevents memory leaks.
- Cleaner and safer code.

---

# Working with Binary Files

Trying to read a binary file using text mode results in an error.

❌ Incorrect:

```python
with open("test.png", "r") as file:
    print(file.read())
```

✔ Correct:

```python
with open("test.png", "rb") as file:
    data = file.read()
```

Writing a binary file:

```python
with open("test.png", "rb") as source:

    with open("copy.png", "wb") as destination:

        destination.write(source.read())
```

This creates a copy of the binary file.

---

# Reading and Processing File Data

Suppose `file.txt` contains:

```text
A=10
B=15
C=20
D=9
```

Program:

```python
with open("file.txt", "r") as file:

    lines = file.readlines()

total = 0

for line in lines:

    value = int(line.split("=")[1])

    if value % 2 != 0:
        total += value

print(total)
```

**Output:**

```python
24
```

Explanation:

- `readlines()` reads all lines.
- `split("=")` separates the variable name and value.
- `int()` converts the value to an integer.
- Only odd numbers are added to `total`.

---

# Summary

- Files are of two types: **Text** and **Binary**.
- `open()` is used to access files.
- `r`, `w`, `a`, `rb`, and `wb` are commonly used file modes.
- `read()`, `readline()`, and `readlines()` are used for reading files.
- File operations use a **file pointer**.
- `with open()` automatically closes files and is the recommended approach.
- Binary files should always be opened using binary modes.
- File contents can be processed just like any other Python data.