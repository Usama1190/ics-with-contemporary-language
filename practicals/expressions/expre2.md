# Math Expressions in Python

Solving various mathematical expressions in Python, covering arithmetic, algebra, logarithms, and physics-related formulas. Each expression includes assumptions, step-by-step breakdowns, and Python code.

---

## Expression 1:

**`y = x**3 + 4 / 12`**

Assume: `x = 2`

```
x = 2
y = x**3 + 4 / 12
```

Steps:

* `x**3 = 8`
* `4 / 12 = 0.333...`
* `8 + 0.333 = 8.333...`

**Result:** `y ≈ 8.33`

---

## Expression 2:

**`y = x**2 + math.log(x) + 6`**

Assume: `x = 2`

```
import math
x = 2
y = x**2 + math.log(x) + 6
```

Steps:

* `x**2 = 4`, `log(2) ≈ 0.693`
* `4 + 0.693 + 6 = 10.693`

**Result:** `y ≈ 10.693`

---

## Expression 3:

**`a = b * x**2 - c * x / d`**

Assume: `b=2, x=3, c=4, d=2`

```
b, x, c, d = 2, 3, 4, 2
a = b * x**2 - c * x / d
```

Steps:

* `x**2 = 9`, `2 * 9 = 18`
* `4 * 3 = 12`, `12 / 2 = 6`
* `18 - 6 = 12`

**Result:** `a = 12`

---

## Expression 4:

**`v = math.e * abs(A * B)`**

Assume: `A = -3`, `B = 2`

```
import math
A, B = -3, 2
v = math.e * abs(A * B)
```

Steps:

* `A * B = -6`, `abs(-6) = 6`
* `e * 6 ≈ 2.718 * 6 = 16.308`

**Result:** `v ≈ 16.308`

---

## Expression 5:

**`z = 1 / x + 1 / (x - a)`**

Assume: `x = 4`, `a = 2`

```
x, a = 4, 2
z = 1 / x + 1 / (x - a)
```

Steps:

* `1/4 = 0.25`, `1/2 = 0.5`
* `0.25 + 0.5 = 0.75`

**Result:** `z = 0.75`

---

## Expression 6:

**`f = (x + y) * (x - y)`**

Assume: `x = 10`, `y = 4`

```
x, y = 10, 4
f = (x + y) * (x - y)
```

**Result:** `f = 84`

---

## Expression 7:

**`k = (a**2 + b**2) / (a + b)`**

Assume: `a = 2`, `b = 3`

```
a, b = 2, 3
k = (a**2 + b**2) / (a + b)
```

**Result:** `k = 2.6`

---

## Expression 8:

**`m = math.sqrt(x**2 + y**2)`**

Assume: `x = 3`, `y = 4`

```
import math
x, y = 3, 4
m = math.sqrt(x**2 + y**2)
```

**Result:** `m = 5`

---

## Expression 9:

**`n = (math.log10(a) + math.log10(b)) / math.log10(c)`**

Assume: `a = 100`, `b = 10`, `c = 10`

```
import math
a, b, c = 100, 10, 10
n = (math.log10(a) + math.log10(b)) / math.log10(c)
```

**Result:** `n = 3`

---

## Expression 10:

**`area = math.pi * r**2`**

Assume: `r = 5`

```
import math
r = 5
area = math.pi * r**2
```

**Result:** `area ≈ 78.54`

---

## Expression 11:

**`p = ((x + y) / (x * y)) + 1`**

Assume: `x = 2`, `y = 3`

```
x, y = 2, 3
p = ((x + y) / (x * y)) + 1
```

**Result:** `p ≈ 1.833`

---

## Expression 12:

**`E = m * c**2`**

Assume: `m = 2`, `c = 3 * 10**8`

```
m = 2
c = 3 * 10**8
E = m * c**2
```

**Result:** `E = 1.8e+17`

---

## Expression 13:

**`s = u * t + 0.5 * a * t**2`**

Assume: `u = 5`, `t = 4`, `a = 2`

```
u, t, a = 5, 4, 2
s = u * t + 0.5 * a * t**2
```

**Result:** `s = 36`

---

## Expression 14:

**`q = a**3 + b**3 - 3 * a * b`**

Assume: `a = 2`, `b = 3`

```
a, b = 2, 3
q = a**3 + b**3 - 3 * a * b
```

**Result:** `q = 17`

---

## Expression 15:

**`T = (x**2 + y**2 + z**2) / 3`**

Assume: `x = 3`, `y = 4`, `z = 5`

```
x, y, z = 3, 4, 5
T = (x**2 + y**2 + z**2) / 3
```

**Result:** `T ≈ 16.67`

---

This guide is part of the CSSE-305 Practical Python Practice series.

**Author:** Usama Israr Khan
**Institution:** UBIT, University of Karachi
**Semester:** 1st

---

Want to add more expressions or convert these into Python files? Let us know!
