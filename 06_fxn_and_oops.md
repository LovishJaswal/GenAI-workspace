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

# Classes and Objects (OOP)

A class is a blueprint for creating objects.

Example:

```python
class ABC:
    a = 10

obj = ABC()

print(obj.a)
```

Output:

```python
10
```

---

## Constructor (`__init__`)

`__init__()` is called automatically whenever an object is created.

```python
class Car:

    def __init__(self):
        print("Car Created")

c = Car()
```

Output:

```python
Car Created
```

> `self` always refers to the current object.

---

# Calculator Class

```python
class Calculator:

    def add(self, a, b):
        print(a + b)

    def subtract(self, a, b):
        print(a - b)

op1 = Calculator()
op1.add(2, 44)

op2 = Calculator()
op2.subtract(5, 3)
```

Output:

```python
46
2
```

---

# Static Methods

A static method belongs to the class rather than any object.

- Does **not** receive `self`.
- Cannot directly access instance variables.

```python
class ABC:

    @staticmethod
    def add(a, b):
        print(a + b)

a = ABC()

a.add(3, 2)
```

Output:

```python
5
```

---

# Difference Between Static and Instance Methods

| Instance Method | Static Method |
|----------------|---------------|
| Uses `self` | Does not use `self` |
| Can access instance variables | Cannot directly access instance variables |
| Called using an object | Can be called using object or class |
| Works on object data | Independent of object data |

Example:

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

    @staticmethod
    def greet():
        print("Welcome!")

s = Student("Lovish")

s.show()
s.greet()
```

---

# Important Note

If a class has both static and instance methods:

- Instance methods can access:
  - `self`
  - Instance variables
  - Class variables

- Static methods:
  - Cannot use `self`
  - Can only access class variables using the class name.

Example:

```python
class ABC:

    a = 10

    def show(self):
        print(self.a)

    @staticmethod
    def display():
        print(ABC.a)
```

Here,

```python
self.a
```

works only inside instance methods.

Inside static methods, use

```python
ABC.a
```

instead.
## Real Use Case of Static Methods

Static methods are useful when a function performs an operation that is related to the class but does **not** depend on a specific object.

Example: Converting kilograms to pounds.

```python
class WeightConverter:

    @staticmethod
    def kg_to_pounds(kg):
        return kg * 2.20462

print(WeightConverter.kg_to_pounds(10))
```

**Output:**

```python
22.0462
```

A static method is appropriate here because the conversion formula is the same for every object and does not require instance data.

---

# Inheritance

Inheritance allows one class to acquire the properties and methods of another class.

- The existing class is called the **Parent (Base) Class**.
- The new class is called the **Child (Derived) Class**.

Syntax:

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

## Method Overriding

If both the parent and child classes have methods (or constructors) with the same name, the child's version overrides the parent's version.

Example:

```python
class Parent:

    def __init__(self):
        print("Parent class constructor")

class Child(Parent):

    def __init__(self):
        print("Child class constructor")

obj = Child()
```

**Output:**

```python
Child class constructor
```

Since the child class defines its own constructor, the parent's constructor is not called automatically.

---

# The `super()` Function

`super()` is used to access methods and constructors of the parent class.

Example:

```python
class Parent:

    def __init__(self, a, b):
        print("The sum of a and b is:", a + b)

    def greet(self):
        print("Hello from parent class")

class Child(Parent):

    def __init__(self):
        super().__init__(4, 6)
        super().greet()
        print("Hello from child class")

obj = Child()
```

**Output:**

```python
The sum of a and b is: 10
Hello from parent class
Hello from child class
```

Without `super()`, only the child's constructor would execute.

---

# Inheritance Example

```python
class Vehicle:

    def number_of_tires(self, tires):
        print("Number of tires:", tires)

    def fuel_type(self, fuel):
        print("Fuel type:", fuel)

class Car(Vehicle):

    def model(self, year):
        print("Model:", year)

alto = Car()

alto.model(2004)
alto.number_of_tires(4)
alto.fuel_type("Petrol")
```

**Output:**

```python
Model: 2004
Number of tires: 4
Fuel type: Petrol
```

Here, the `Car` class inherits all methods from the `Vehicle` class.

---

# Getter and Setter

Getter and Setter methods provide controlled access to object attributes.

Python provides the `@property` decorator to implement getters and the `@<property>.setter` decorator for setters.

Example:

```python
class ABCD:

    def __init__(self):
        self._value = 0

    @property
    def a(self):
        return self._value

    @a.setter
    def a(self, value):
        self._value = value

obj = ABCD()

obj.a = 12

print(obj.a)
```

**Output:**

```python
12
```

### Why use Getters and Setters?

- Control how attributes are accessed.
- Validate data before storing it.
- Hide internal implementation details.
- Improve encapsulation.

---

# Multiple Inheritance

A class can inherit from more than one parent class.

Syntax:

```python
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
```

Example:

```python
class Father:

    def father_skill(self):
        print("Driving")

class Mother:

    def mother_skill(self):
        print("Cooking")

class Child(Father, Mother):
    pass

obj = Child()

obj.father_skill()
obj.mother_skill()
```

**Output:**

```python
Driving
Cooking
```

Python resolves method conflicts using the **Method Resolution Order (MRO)**.

You can check the MRO using:

```python
print(Child.mro())
```

or

```python
help(Child)
```