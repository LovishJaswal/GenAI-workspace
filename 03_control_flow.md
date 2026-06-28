# Day 03 – Python Basics & Control Flow

## Training

**Course:** Python + Generative AI

**Day:** 03

---

# Topics Covered

- Variables
- Arithmetic Operators
- User Input
- Type Casting
- Formatted Strings (f-Strings)
- Data Types
- Conditional Statements
- Comparison Operators
- Calculator Program
- `for` Loop
- `range()`
- `while` Loop
- `pass` Statement
- Logical Operators

---

# Variables

Variables are used to store data in memory.

### Example

```python
a = 5
b = 6
c = a + b
```

---

# Arithmetic Operators

| Operator | Description |
|----------|-------------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulus (Remainder) |
| `//` | Floor Division |
| `**` | Exponentiation (Power) |

---

# User Input

The `input()` function accepts input from the user.

> **Note**
>
> `input()` always returns a **string**.

### Example

```python
name = input("Enter your name: ")
```

For numerical calculations, convert the input into the required type.

```python
age = int(input("Enter your age: "))
```

---

# Type Conversion

Common conversion functions:

- `int()`
- `float()`
- `str()`
- `bool()`

### Example

```python
num = int(input("Enter a number: "))
```

---

# Formatted Strings (f-Strings)

f-Strings allow variables to be embedded directly inside strings.

### Example

```python
name = "Lovish"

print(f"Hello, {name}")
```

---

# Checking Data Types

Use the `type()` function to determine the type of an object.

### Example

```python
a = 10

print(type(a))
```

---

# Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not Equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or Equal to |
| `<=` | Less than or Equal to |

---

# Conditional Statements

Python provides three decision-making statements:

- `if`
- `elif`
- `else`

### Example

```python
age = 15

if age > 10:
    print("You are not a kid")
elif age > 5:
    print("You are a kid")
else:
    print("You are a toddler")
```

---

# Calculator Program

A simple calculator was created using conditional statements.

Supported operations:

- Addition
- Subtraction
- Multiplication
- Division
- Modulus

### Example

```python
num1 = int(input("Enter your first operand: "))
num2 = int(input("Enter your second operand: "))
op = input("Enter your operator: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "%":
    print(num1 % num2)
```

---

# The `for` Loop

A `for` loop is used when the number of iterations is known.

### Example

```python
for i in range(1, 5):
    print(i)
```

---

# The `range()` Function

The `range()` function generates a sequence of numbers.

```python
range(start, stop, step)
```

Example:

```python
range(1, 5)
```

Output:

```text
1
2
3
4
```

> **Note**
>
> The `stop` value is **not included**.

---

# Printing Even Numbers

### Example

```python
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
```

---

# Logical Operators

Python uses the following logical operators:

| Operator | Description |
|----------|-------------|
| `and` | Logical AND |
| `or` | Logical OR |
| `not` | Logical NOT |

> **Note**
>
> Python does **not** use `&&` or `||` like C/C++ or Java.

---

# The `pass` Statement

The `pass` statement is a placeholder.

It allows you to define an empty block without causing an error.

### Example

```python
if True:
    pass
```

---

# The `while` Loop

A `while` loop executes repeatedly as long as its condition remains `True`.

### Example

```python
i = 0

while i < 10:
    print(i)
    i += 1
```

---

# Calculator using a `while` Loop

The calculator was modified to run continuously until the user decided to exit.

### Example

```python
per = None

while per != "QUIT" and per != "quit":

    num1 = int(input("Enter your first operand: "))
    num2 = int(input("Enter your second operand: "))
    op = input("Enter your operator: ")

    if op == "+":
        print(num1 + num2)

    elif op == "-":
        print(num1 - num2)

    elif op == "*":
        print(num1 * num2)

    elif op == "/":
        print(num1 / num2)

    elif op == "%":
        print(num1 % num2)

    per = input("Enter 'QUIT' to exit or press Enter to continue: ")
```

This allows the calculator to perform multiple calculations without restarting the program.

---

# Programs Developed

- Variable Examples
- Age Classification Program
- Basic Calculator
- Even Number Generator
- Continuous Calculator using `while` Loop

---

# Key Takeaways

- Variables store data.
- `input()` always returns a string.
- Type conversion is required for numerical input.
- f-Strings simplify string formatting.
- Conditional statements control program flow.
- `for` loops are useful for known iterations.
- `while` loops execute until a condition becomes `False`.
- Python uses `and`, `or`, and `not` instead of `&&` and `||`.
- `pass` acts as a placeholder for empty code blocks.