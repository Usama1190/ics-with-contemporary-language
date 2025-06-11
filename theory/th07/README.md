# Data Structures: Lists, Tuples, Dictionaries

## Introduction

Data structures are used in programming to store and organize data efficiently. Python provides several built-in data structures, with the most commonly used being **Lists**, **Tuples**, and **Dictionaries**.

Each of these has different characteristics and use-cases based on how data is stored and accessed.

---

## Lists

### What is a List?

A list in Python is a collection that is **ordered**, **changeable (mutable)**, and **allows duplicate elements**.

```python
fruits = ["apple", "banana", "cherry"]
```

### Features

* Ordered
* Mutable (can be changed)
* Allows duplicates
* Indexed (starts from 0)

### Common Operations

```python
# Accessing
print(fruits[1])  # banana

# Modifying
fruits[0] = "orange"

# Adding
fruits.append("mango")

# Removing
fruits.remove("banana")

# Looping
for fruit in fruits:
    print(fruit)
```

---

## Tuples

### What is a Tuple?

A tuple is similar to a list, but it is **immutable** – once created, it cannot be changed.

```python
coordinates = (10, 20)
```

### Features

* Ordered
* Immutable
* Allows duplicates
* Indexed

### When to Use

* When the data should not change (e.g., coordinates, constants)

### Example

```python
# Accessing elements
print(coordinates[0])  # 10

# Tuple unpacking
x, y = coordinates
print(x, y)
```

---

## Dictionaries

### What is a Dictionary?

A dictionary stores data in **key-value pairs**. It is **unordered (in versions <3.7)**, **mutable**, and **does not allow duplicate keys**.

```python
student = {
    "name": "Ali",
    "age": 22,
    "grade": "A"
}
```

### Features

* Key-value based
* Mutable
* No duplicate keys
* Fast access via keys

### Common Operations

```python
# Accessing
print(student["name"])

# Modifying
student["age"] = 23

# Adding new key
student["email"] = "ali@example.com"

# Removing
del student["grade"]

# Looping
for key, value in student.items():
    print(key, value)
```

---

## Comparison Table

| Feature    | List    | Tuple   | Dictionary        |
| ---------- | ------- | ------- | ----------------- |
| Ordered    | Yes     | Yes     | Python 3.7+: Yes  |
| Mutable    | Yes     | No      | Yes               |
| Indexed    | Yes     | Yes     | By keys           |
| Duplicates | Allowed | Allowed | Keys: Not allowed |
| Syntax     | `[]`    | `()`    | `{}`              |

---

## Real-Life Use Cases

| Use Case                  | Recommended Structure |
| ------------------------- | --------------------- |
| Shopping cart items       | List                  |
| Geographical coordinates  | Tuple                 |
| Storing user profiles     | Dictionary            |
| RGB color value (fixed)   | Tuple                 |
| API response (keyed data) | Dictionary            |

---

## Practice Exercises

1. Create a list of 5 favorite movies and print each using a loop.
2. Store a tuple representing (latitude, longitude) of your city.
3. Create a dictionary to represent a book with title, author, and year.
