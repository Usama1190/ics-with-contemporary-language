# Functions and Modularity

## Introduction

Functions and modularity are foundational concepts in programming that promote code reusability, clarity, and maintainability. By breaking large problems into smaller functions or modules, we can manage complex programs more easily.

---

## What is a Function?

A function is a reusable block of code that performs a specific task. Functions help avoid repetition, improve readability, and make testing easier.

### Basic Structure of a Function (Python)

```python
def greet(name):
    return f"Hello, {name}!"
```

* `def`: Keyword used to define a function.
* `greet`: Name of the function.
* `name`: Parameter.
* `return`: Sends a result back to the caller.

### Function Call

```python
print(greet("Alice"))  # Output: Hello, Alice!
```

---

## Parameters and Arguments

* **Parameter**: Variable listed in function definition.
* **Argument**: Actual value passed to the function.

```python
def add(x, y):  # x and y are parameters
    return x + y

add(2, 3)  # 2 and 3 are arguments
```

---

## Return Values

A function can return a result using the `return` statement.

```python
def square(n):
    return n * n
```

---

## Types of Functions

| Type               | Description                              |
| ------------------ | ---------------------------------------- |
| Built-in Functions | Provided by the language (e.g., `len()`) |
| User-defined       | Created by the programmer                |
| Lambda Functions   | Anonymous, one-line functions            |

### Lambda Example

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

## What is Modularity?

Modularity means dividing a program into independent modules (or files), each handling a specific responsibility. This improves readability, debugging, and collaboration.

### Benefits of Modularity

* Easier to test and debug
* Promotes reuse of code
* Easier team collaboration
* Faster development

---

## Modular Programming Example

**math\_utils.py**

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
```

**main.py**

```python
import math_utils

print(math_utils.add(10, 5))       # Output: 15
print(math_utils.subtract(10, 5))  # Output: 5
```

---

## Scope of Variables

* **Local Scope**: Variable inside a function.
* **Global Scope**: Variable defined outside any function.

```python
x = 5  # Global

def test():
    x = 10  # Local
    print(x)

test()      # Output: 10
print(x)    # Output: 5
```

---

## Real-Life Analogy

Think of a function like a **coffee machine**:

* You give it inputs (water, coffee powder).
* It performs a task (brewing).
* It gives output (coffee).
* You can reuse the machine anytime.

---

## Summary Table

| Concept    | Description                             |
| ---------- | --------------------------------------- |
| Function   | A reusable block of code                |
| Parameter  | Input variable in a function definition |
| Argument   | Actual value passed to the function     |
| Return     | Keyword to send back output             |
| Modularity | Breaking code into independent modules  |
| Scope      | Visibility of variables (local/global)  |

---

## Practice Exercises

1. Write a function to calculate the factorial of a number.
2. Create a module `calculator.py` with `add`, `subtract`, `multiply`, and `divide` functions.
3. Build a program that uses a function to check if a number is even or odd.
