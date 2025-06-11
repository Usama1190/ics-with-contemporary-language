# Python Expressions Practice

This section of the course covers **Python expressions**. Each example below includes:

* A real-world style expression
* Python code
* Step-by-step explanation

---

## 📘 Expressions Covered

### Expression 1:

**`y = x² + log(x) + 6`**

Let’s assume `x = 2`

```python
import math

x = 2
y = x**2 + math.log(x) + 6
```

**Breakdown:**

* `x²` → `2² = 4`
* `log(x)` → `log(2) ≈ 0.6931`
* Add all: `4 + 0.6931 + 6 ≈ 10.6931`

Final Answer: `y ≈ 10.6931`

---

### Expression 2:

**`a = b·x² - c·x / d`**

Let’s assume: `b = 3`, `c = 4`, `d = 2`, `x = 5`

```python
b, c, d, x = 3, 4, 2, 5
a = b * x**2 - c * x / d
```

**Breakdown:**

* `x²` → `25`
* `b * x²` → `3 * 25 = 75`
* `c * x` → `4 * 5 = 20`
* `20 / d` → `20 / 2 = 10`
* Final: `75 - 10 = 65`

Final Answer: `a = 65`

---

### Expression 3:

**`v = e * |A * B|`**

Let’s assume: `A = 4`, `B = -5`

```python
import math

A, B = 4, -5
v = math.e * abs(A * B)
```

**Breakdown:**

* `A * B` → `4 * -5 = -20`
* `abs(-20)` → `20`
* `math.e * 20` → `2.718 * 20 = 54.36`

Final Answer: `v ≈ 54.36`

---

### Expression 4:

**`z = 1/x + 1/(x - a)`**

Let’s assume `x = 3`, `a = 2`

```python
x, a = 3, 2
z = (1 / x) + (1 / (x - a))
```

**Breakdown:**

* `1 / x` → `1/3 ≈ 0.333`
* `x - a` → `3 - 2 = 1`
* `1 / 1 = 1`
* Add: `0.333 + 1 = 1.333`

Final Answer: `z ≈ 1.333`

---

### Expression 5:

**`y = x * x - x`**

Let’s assume `x = 6`

```python
x = 6
y = x * x - x
```

**Breakdown:**

* `x * x = 36`
* `36 - 6 = 30`

Final Answer: `y = 30`
