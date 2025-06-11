# Expressions in Python

Expressions are the building blocks of any programming language. In Python, an **expression** is a combination of variables, values, operators, and function calls that can be evaluated to produce another value.

---

## What is an Expression?

An expression in Python performs some computation or action and returns a result. It may involve:
- Constants or literals (e.g., `2`, `3.14`)
- Variables (e.g., `x`, `y`)
- Operators (`+`, `-`, `*`, `/`, `**`)
- Function calls (e.g., `math.sqrt(x)`, `math.log(x)`)

**Example:**
```python
y = x**2 + math.log(x) + 6
```

This expression uses:

* A variable x
* The exponentiation operator **
* A mathematical function log
* Addition and a constant

## Python Operators Commonly Used in Expressions

| Operator | Description              | Example       |
| -------- | ------------------------ | ------------- |
| `+`      | Addition                 | `x + y`       |
| `-`      | Subtraction              | `x - y`       |
| `*`      | Multiplication           | `x * y`       |
| `/`      | Division                 | `x / y`       |
| `**`     | Exponentiation (power)   | `x**2`        |
| `%`      | Modulus (remainder)      | `x % y`       |
| `()`     | Parentheses (precedence) | `(a + b) * c` |

## Import Required Math Functions

Some expressions require functions like square root, logarithm, etc. These are available in Python's built-in `math` module.

```
import math
```

### Expression Examples in Python

```
import math

# 1. Basic polynomial
x = 2
y = x**2 + math.log(x) + 6
print("y =", y)

# 2. Algebraic with multiple variables
b, c, d, x = 3, 4, 2, 5
a = b * x**2 - c * x / d
print("a =", a)

# 3. Absolute value with multiplication
A, B = 4, -5
v = math.e * abs(A * B)
print("v =", v)

# 4. Rational expression
x, a = 3, 2
z = (1 / x) + (1 / (x - a))
print("z =", z)

# 5. Quadratic simplified
x = 6
y = x * x - x
print("y =", y)

# 6. Square root with exponent
x = 9
result = math.sqrt(x) + x**1.5
print("Result =", result)

# 7. Trigonometric expression
theta = math.pi / 4
res = math.sin(theta) + math.cos(theta)
print("res =", res)

# 8. Logarithmic and exponent
x = 10
out = math.exp(x) / math.log(x)
print("out =", out)

# 9. Mixed operations
a, b, c = 5, 2, 3
value = (a + b)**2 - (c * b)
print("value =", value)

# 10. Exponential decay
t, k = 2, 0.1
N = 100 * math.exp(-k * t)
print("N =", N)

# 11. Cube root approximation
x = 27
cube_root = x ** (1/3)
print("cube_root =", cube_root)

# 12. Distance formula (2D)
x1, y1 = 2, 3
x2, y2 = 5, 7
dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance =", dist)

# 13. Compound interest
P, r, n, t = 1000, 0.05, 12, 2
A = P * (1 + r/n)**(n*t)
print("Compound Interest =", A)

# 14. Area of a triangle using Heron's formula
a, b, c = 5, 6, 7
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Triangle Area =", area)

# 15. Fahrenheit to Celsius conversion
F = 98.6
C = (F - 32) * 5/9
print("Celsius =", C)
```

### Summary

* Python expressions are combinations of variables, operators, and functions.

* Use the math module for advanced calculations like square roots, logs, trigonometry, etc.

* Expressions are useful for real-world computations like geometry, physics, and finance.
