# Data Types and Variables

## What Are Variables?

A **variable** is a named container used to store data in a program. It can hold values like numbers, text, or more complex structures depending on the language you're using.

Think of a variable as a labeled box: you put something in it (a value), and later you can use, change, or read that value using the box's label (the variable name).

**Example (in Python):**
```python
age = 25
name = "Alice"
is_student = True
```

## Why Are Variables Important?

- They help store and manipulate data.
- They make your code reusable and dynamic.
- Variables improve the readability and organization of code.

---

## What Are Data Types?

**Data types** define the kind of data a variable can hold. Different types are used for different purposes — numbers for math, strings for text, etc.

Every variable has a data type that determines:
- The kind of data it stores
- The operations you can perform on it
- The amount of memory it takes

---

## Common Data Types in Programming

| Data Type      | Description                   | Example                |
|----------------|-------------------------------|------------------------|
| **Integer**    | Whole numbers                 | `42`, `-7`, `1000`     |
| **Float**      | Numbers with decimal points   | `3.14`, `-0.99`        |
| **String**     | Sequence of characters (text) | `"Hello"`, `'123'`     |
| **Boolean**    | Logical values — true or false| `True`, `False`        |
| **Array/List** | Ordered collection of items   | `[1, 2, 3]`, `["a", "b"]`|
| **Object/Dict** | Collection of key-value pairs (maps)| `{"name": "Ali"}`|
| **Null/None**   | No value / empty             | `null`, `None`         |

---

## Declaring Variables in Different Languages

### Python
```python
name = "John"
age = 30
is_active = True
```

### JavaScript
```javascript
let name = "John";
const age = 30;
var isActive = true;
```

### Java
```java
String name = "John";
int age = 30;
boolean isActive = true;
```

---

## Dynamic vs Static Typing

| Type System    | Description                                                | Example Languages       |
|----------------|------------------------------------------------------------|--------------------------|
| **Static Typing** | Data types are declared and checked at compile time     | Java, C++, TypeScript    |
| **Dynamic Typing** | Data types are determined at runtime                   | Python, JavaScript       |

**Example:**
```python
# Dynamic typing (Python)
x = 10       # int
x = "Hello"  # now a string — no error
```

```java
// Static typing (Java)
int x = 10;
x = "Hello"; // Error: incompatible types
```

---

## Variable Naming Rules (Best Practices)

- Use meaningful names: `age`, `user_name`, `is_valid`
- Start with a letter (A-Z or a-z) or underscore (_)
- Avoid reserved keywords (`class`, `if`, `return`)
- Use snake_case (Python) or camelCase (JavaScript) based on convention
- Be consistent and descriptive

---

## Type Conversion (Casting)

Sometimes you need to convert data from one type to another:

### Python
```python
str_num = "123"
int_num = int(str_num)  # Converts string to integer
```

### JavaScript
```javascript
let str = "3.14";
let num = parseFloat(str); // Converts to float
```

---

## Memory and Variable Storage

Variables are stored in RAM when a program runs. Each variable occupies memory depending on its data type:

| Type     | Typical Size |
|----------|--------------|
| int      | 4 bytes      |
| float    | 4–8 bytes    |
| bool     | 1 byte       |
| char     | 1 byte       |

---

## Real-World Example: Shopping Cart

```python
item_name = "Shoes"
quantity = 2
price = 99.99
total_cost = quantity * price  # = 199.98
```

Here:
- `item_name` is a **string**
- `quantity` is an **integer**
- `price` is a **float**
- `total_cost` is the result of a float * int

---

## Summary

| Concept       | Description                              |
|---------------|------------------------------------------|
| Variable       | A named placeholder for data             |
| Data Type      | Classification of the kind of data       |
| Static Typing  | Types declared at compile-time           |
| Dynamic Typing | Types assigned during runtime            |
| Casting        | Converting one data type to another      |

---

## Practice Activity

- Declare variables of each data type in python language.
- Try converting strings to integers and vice versa.
- Build a basic calculator using variables and user input.
---
