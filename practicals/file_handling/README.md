## Practical: File Handling in Python

This practical introduces how to work with files using Python's built-in `open()` function. You will learn to read, write, and append to files.

---

### Example 1: Writing to a File
```python
with open("output.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("Welcome to Python file handling.")
```

### Summary Table

| Mode          | Description                   |
| ------------- | ----------------------------- |
| `"r"`         | Read (default)                |
| `"w"`         | Write (overwrite)             |
| `"a"`         | Append                        |
| `"x"`         | Create (fails if file exists) |
| `.read()`     | Reads the entire content      |
| `.readline()` | Reads one line                |
| `.write()`    | Writes a string               |
