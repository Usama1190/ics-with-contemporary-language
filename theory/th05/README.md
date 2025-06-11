# Logic and Control Flow

## Introduction
Logic and Control Flow are essential concepts in programming that help make decisions, repeat tasks, and execute code conditionally. These tools allow developers to control the direction and behavior of a program based on specific conditions.

## What is Logic in Programming?
Logic refers to the use of conditional statements and boolean expressions (true/false values) to make decisions in a program.

**Example:**

```python
is_raining = True
if is_raining:
    print("Take an umbrella")
```

Here, the program checks a condition (`is_raining`) and acts accordingly. Logic is built using boolean operators and comparisons.

## Boolean Expressions
Boolean expressions return either `True` or `False`.

### Comparison Operators

| Operator | Meaning          | Example   |
|----------|------------------|-----------|
| `==`     | Equal to         | `a == b`  |
| `!=`     | Not equal to     | `a != b`  |
| `>`      | Greater than     | `a > b`   |
| `<`      | Less than        | `a < b`   |
| `>=`     | Greater or equal | `a >= b`  |
| `<=`     | Less or equal    | `a <= b`  |

### Logical Operators

| Operator | Meaning              | Example             |
|----------|----------------------|---------------------|
| `and`    | True if both are true| `a > 5 and b < 10`  |
| `or`     | True if one is true  | `a > 5 or b < 10`   |
| `not`    | Reverses the result  | `not a > 5`         |

## What is Control Flow?
Control flow defines the order in which instructions, statements, and functions are executed in a program. It includes:

- Conditional Statements (`if`, `elif`, `else`)
- Loops (`for`, `while`)
- Break / Continue / Pass

## Conditional Statements
Allow a program to take different actions based on different conditions.

**Python Example:**

```python
age = 18
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")
```

## Loops (Iteration)
Loops let us repeat a block of code multiple times.

### For Loop

```python
for i in range(5):
    print(i)
```

### While Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## Loop Control Statements

| Keyword   | Description                            |
|-----------|----------------------------------------|
| `break`   | Exit the loop early                    |
| `continue`| Skip to the next iteration             |
| `pass`    | Does nothing (used as a placeholder)   |

**Example:**

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

## Flowchart of Control Flow

- Start
- Check Condition
- If True → Execute Block A
- Else → Execute Block B
- End

## Real-World Example

**Login System Logic:**

```python
username = input("Enter username: ")
if username == "admin":
    print("Access granted")
else:
    print("Access denied")
```

This uses logic and control flow to authenticate users.

## Summary Table

| Concept              | Description                                     |
|----------------------|-------------------------------------------------|
| Logic                | Decision-making using conditions (True/False)   |
| Control Flow         | Directs execution based on logic or repetition  |
| Conditional Statements | `if`, `elif`, `else`                          |
| Loops                | `for`, `while` for repeating tasks              |
| Loop Control         | `break`, `continue`, `pass`                     |

## Practice Exercise

1. Write a program that prints even numbers between 1 and 20 using a `for` loop.
2. Create a login system that checks if a password is correct.
3. Use a `while` loop to keep asking for user input until the correct answer is given.
