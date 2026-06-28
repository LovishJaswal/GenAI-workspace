# Day 06 - Python Functions, Lambda Functions & OOP Basics

---

# Functions

## `*args`

- `*args` allows a function to accept **multiple positional arguments**.
- The received arguments are stored as a **tuple**.

```python
def func_name(n, *nums, b):
    print(nums)

func_name(1, 2, 3, 4, 5, 6, b=7)
```

**Output:**

```python
(2, 3, 4, 5, 6)
```

### Rules

- Positional arguments must come before keyword arguments.
- `*args` should be declared before keyword-only arguments.
- Parameter order should be followed.

General parameter order:

```python
def func(positional, *args, keyword_only, **kwargs):
    pass
```

---

# Keyword Arguments

Keyword arguments allow values to be passed using parameter names.

```python
def fun_name_2(b, c, d):
    print(b, c, d)

fun_name_2(b=2, c=3, d=3)
```

Output:

```python
2 3 3
```

---

# `**kwargs`

- `**kwargs` accepts any number of **keyword arguments**.
- The received arguments are stored as a **dictionary**.

```python
def fun_name_3(**kwargs):
    print(type(kwargs))

    total = 0

    for x in kwargs.values():
        total += x

    print(total)

fun_name_3(b=2, c=5, d=4)
```

Output:

```python
<class 'dict'>
11
```

---

# Notes

### `*` is an unpack operator

The `*` symbol is **not** a reference operator.

It is called the **unpacking operator**.

Example:

```python
numbers = [1, 2, 3]

print(*numbers)
```

Output:

```python
1 2 3
```

---

If a dictionary is unpacked using `*`, only the **keys** are unpacked.

```python
d = {
    "a": 1,
    "b": 2
}

print(*d)
```

Output:

```python
a b
```

If unpacked using `**`, both keys and values are passed as keyword arguments.

```python
def show(a, b):
    print(a, b)

d = {
    "a": 10,
    "b": 20
}

show(**d)
```

Output:

```python
10 20
```

---

## Parameter Order

Always follow this order:

```text
Positional arguments
      ↓
*args
      ↓
Keyword-only arguments
      ↓
**kwargs
```

---

# Lambda Functions

Lambda functions are anonymous (nameless) functions written in a single line.

Syntax:

```python
lambda arguments: expression
```

Example:

```python
a = lambda x: x + 1

print(a(5))
```

Output:

```python
6
```

---

Returning a lambda from a function

```python
def abc():
    a = lambda a, b, c: a + b + c
    return a

a = abc()

print(a(1, 2, 3))
```

Output:

```python
6
```

---

Equivalent without lambda

```python
def abc():

    def add(a, b):
        return a + b

    return add

func = abc()

print(func(1, 2))
```

Output:

```python
3
```

---

## Doubt

> Multiple lambda functions together can be stored inside a tuple, list, or dictionary.

Example:

```python
funcs = (
    lambda x: x + 1,
    lambda x: x * 2
)
```

Here,

```python
type(funcs)
```

returns

```python
tuple
```

If only one lambda is assigned,

```python
f = lambda x: x + 1
```

then

```python
type(f)
```

returns

```python
<class 'function'>
```

---