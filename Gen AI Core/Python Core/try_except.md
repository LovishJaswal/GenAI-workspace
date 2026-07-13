# Exception Handling

---

# Introduction

Exception handling allows a program to handle runtime errors gracefully without terminating unexpectedly.

Python provides the `try`, `except`, `else`, and `finally` blocks for exception handling.

---

# Basic Exception Handling

Syntax:

```python
try:
    # Code that may raise an exception
except Exception as e:
    # Code to handle the exception
```

Example:

```python
try:
    print(6 / 0)

except Exception as e:
    print(e)

print("Hello")
```

**Output:**

```text
division by zero
Hello
```

The exception is caught, allowing the program to continue executing.

---

# Execution Flow

If an exception occurs inside the `try` block:

- The remaining statements inside the `try` block are skipped.
- Control immediately moves to the matching `except` block.
- After handling the exception, execution continues normally.

Example:

```python
try:
    print(6 / 0)
    print("This will not execute")

except Exception as e:
    print(e)

print("Program continues...")
```

---

# Handling File Exceptions

```python
try:
    file = open("file.txt", "r")

    print(file.read())
    print("abc")

except Exception as e:
    print(e)

finally:
    file.close()
```

The `finally` block executes whether or not an exception occurs.

---

# The `finally` Block

The `finally` block is always executed.

It is commonly used for:

- Closing files
- Closing database connections
- Releasing resources
- Cleaning up memory

Example:

```python
try:
    print("Inside try")

finally:
    print("Always executed")
```

---

# Handling Specific Exceptions

Instead of catching every exception, Python allows handling specific exception types.

Example:

```python
try:
    print(6 / 0)

except ZeroDivisionError:
    print("You cannot divide by zero")

except TypeError:
    print("You entered different datatypes")

except Exception:
    print("Something went wrong")
```

Different exceptions are handled by different `except` blocks.

---

# Raising Exceptions

Python allows programmers to generate exceptions manually using the `raise` keyword.

Syntax:

```python
raise Exception("Error Message")
```

Example:

```python
try:

    number = int(input("Enter an even number: "))

    if number % 2 != 0:
        raise Exception("Number must be even")

except Exception as e:
    print(e)
```

If the entered number is odd, the custom exception is raised.

---

# Custom Validation Example

```python
try:

    age = int(input("Enter your age: "))

    if age < 18:
        raise Exception("Age must be greater than or equal to 18")

    elif age > 110:
        raise Exception("Age must be less than 110")

    else:
        print("Congrats! Your voter card is ready.")

except ValueError:
    print("Age must be an integer")

except Exception as e:
    print(e)
```

Possible outputs:

```text
Enter your age: 15

Age must be greater than or equal to 18
```

or

```text
Enter your age: abc

Age must be an integer
```

---

# Common Built-in Exceptions

| Exception | Description |
|-----------|-------------|
| `ZeroDivisionError` | Division by zero |
| `TypeError` | Operation performed on incompatible data types |
| `ValueError` | Invalid value passed to a function |
| `FileNotFoundError` | File does not exist |
| `IndexError` | Index out of range |
| `KeyError` | Dictionary key not found |
| `AttributeError` | Attribute or method does not exist |
| `Exception` | Base class for most exceptions |

---

# Best Practices

- Catch specific exceptions whenever possible.
- Avoid using a bare `except` block.
- Use `finally` to release resources.
- Raise exceptions only when necessary.
- Keep `try` blocks as small as possible.

---

# Summary

- `try` contains code that may raise an exception.
- `except` handles the exception.
- `finally` always executes.
- `raise` is used to generate custom exceptions.
- Specific exceptions should be preferred over catching every exception.
- Exception handling prevents programs from crashing unexpectedly.