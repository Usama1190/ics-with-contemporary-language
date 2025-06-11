# Binary and Number Systems

## What is a Number System?

A **number system** is a way to represent and express numbers using symbols (digits) according to specific rules.

* Humans commonly use the **Decimal** system (base-10), which uses digits 0–9.
* Computers, however, operate using the **Binary** system (base-2), which uses only 0 and 1.

---

## Types of Number Systems

| Name            | Base | Digits Used | Common Use                       |
| --------------- | ---- | ----------- | -------------------------------- |
| **Binary**      | 2    | 0, 1        | Computers, electronics           |
| **Octal**       | 8    | 0–7         | Early computing                  |
| **Decimal**     | 10   | 0–9         | Humans (daily use)               |
| **Hexadecimal** | 16   | 0–9, A–F    | Memory, web colors, machine code |

---

## What is the Binary Number System?

The **Binary system** is a base-2 number system that uses only two digits — **0** and **1**. Each digit in a binary number is called a **bit**.

### Example:

Binary Number: `1011`

```
Position:   2^3   2^2   2^1   2^0
Digits:       1     0     1     1
Value:        8  +  0  +  2  +  1  = 11 (Decimal)
```

So, `1011` (binary) = `11` (decimal).

---

## Conversion Between Number Systems

### Binary to Decimal

**Steps:**

1. Write the binary number.
2. Multiply each bit by its power of 2.
3. Add all the values.

**Example:**

```
Binary: 1101
= 1×8 + 1×4 + 0×2 + 1×1 = 13
```

### Decimal to Binary

**Steps:**

1. Divide the decimal number by 2.
2. Write down the remainder (0 or 1).
3. Repeat until the result is 0.
4. Reverse the remainders to get the binary number.

**Example:**

```
Decimal: 10
10 ÷ 2 = 5 remainder 0
5 ÷ 2 = 2 remainder 1
2 ÷ 2 = 1 remainder 0
1 ÷ 2 = 0 remainder 1

Binary: 1010
```

### Decimal to Hexadecimal

**Steps:**

1. Divide the decimal number by 16.
2. Use 0–9 and A–F for remainders.

**Example:**

```
Decimal: 255 → Hex = FF
(16×15 + 15 = 255)
```

---

## Why Do Computers Use Binary?

Computers use binary because all internal operations are based on **electronic signals** — either **on (1)** or **off (0)**.

* **0** = No voltage
* **1** = Voltage present

This system is simple, reliable, and works well with digital electronic components like **transistors**.

---

## Real-World Analogy

**Light Switch = Binary**

* ON = 1
* OFF = 0

Just like turning lights on or off, computers process signals using 0s and 1s.

---

## Real-Life Uses of Binary

| Field           | Example                                         |
| --------------- | ----------------------------------------------- |
| Text Storage    | Letters → Binary using ASCII or Unicode         |
| Images          | Pixels encoded as binary color codes            |
| Music/Audio     | Sound waves stored as binary data               |
| Programming     | Source code compiled into binary (machine code) |
| Networking      | Data packets and IP addresses in binary         |
| Web Development | Colors like `#FF0000` use binary/hex codes      |

---

## Example: Text in Binary using ASCII

| Character | ASCII Decimal | Binary   |
| --------- | ------------- | -------- |
| A         | 65            | 01000001 |
| B         | 66            | 01000010 |
| a         | 97            | 01100001 |
| 1         | 49            | 00110001 |

**"Hi" in Binary:**

* H = `01001000`
* i = `01101001`

---

## Architecture: Binary in Computer System

### Memory

* RAM and storage devices save everything in binary — images, text, music, apps.
* Example: `1001 0110 1111` = part of a file.

### CPU

* Reads binary instructions (machine code).
* Executes them using circuits like ALU (Arithmetic Logic Unit).

### Output Devices

* Convert binary back to human-readable form: text, images, videos, sound.

---

## ⚙️ Step-by-Step Architecture Flow

```text
[User Types "A"]
       ↓
[Keyboard sends binary: 01000001]
       ↓
[CPU receives and stores it in RAM]
       ↓
[Application reads binary and processes it]
       ↓
[Monitor shows "A"]
```

---

## Bit-Length: What is 4-bit, 8-bit, 16-bit?

| Bit Length | Max Binary Value | Decimal Equivalent |
| ---------- | ---------------- | ------------------ |
| 4-bit      | 1111             | 15                 |
| 8-bit      | 11111111         | 255                |
| 16-bit     | 1111111111111111 | 65535              |

More bits = more information that can be represented and processed.

---

## Summary Table

| Term        | Meaning                                           |
| ----------- | ------------------------------------------------- |
| Binary      | Base-2 number system using only 0 and 1           |
| Bit         | A single binary digit (0 or 1)                    |
| Byte        | Group of 8 bits                                   |
| ASCII       | Encoding system that maps text to binary          |
| Hexadecimal | Base-16 system using 0–9 and A–F                  |
| Conversion  | Translating values between different number bases |

---

## Practice Activity

* Convert these **decimals to binary**: `7`, `15`, `25`, `100`
* Convert these **binaries to decimal**: `101`, `1101`, `10010`
* Write the word **"Hi"** in binary using the ASCII table
