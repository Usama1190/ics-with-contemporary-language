# Problem Solving Techniques

## Introduction

Problem-solving is a key skill in programming and computer science. It involves understanding a problem, devising a plan, carrying it out, and evaluating the solution. Effective problem-solving techniques are essential for writing correct, efficient, and maintainable code.

---

## Key Problem Solving Steps

### 1. Understand the Problem
- Read the problem carefully.
- Identify inputs, outputs, and constraints.
- Clarify any unclear requirements.

### 2. Break Down the Problem
- Divide the main problem into smaller sub-problems.
- Tackle each sub-problem individually.

### 3. Plan a Solution
- Choose an appropriate algorithm or strategy.
- Think through the logic before writing code.
- Sketch pseudocode or a flowchart.

### 4. Write the Code
- Implement the plan in a programming language.
- Start with a basic version and improve gradually.

### 5. Test the Solution
- Use test cases to verify correctness.
- Include edge cases and invalid inputs.

### 6. Optimize the Solution
- Improve time and space complexity if possible.
- Refactor repetitive or inefficient code.

---

## Problem Solving Strategies

### Brute Force
- Try all possible solutions.
- Easy to implement but not efficient.

### Divide and Conquer
- Split problem into halves, solve recursively.
- Example: Binary Search, Merge Sort.

### Greedy Approach
- Make the best local choice at each step.
- Works well in optimization problems (e.g., coin change).

### Dynamic Programming
- Store intermediate results to avoid recomputation.
- Useful for problems with overlapping subproblems.

### Backtracking
- Try possible solutions and undo if needed.
- Example: N-Queens, Sudoku solver.

### Pattern Recognition
- Spot patterns or similarities to previously solved problems.

---

## Example Problem: Find Maximum Number in a List

### Problem:
Write a program to find the largest number in a given list of integers.

### Python Solution:
```python
numbers = [4, 9, 2, 5, 7]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Maximum number:", max_num)
```

#### Practice Techniques
Start with small problems (e.g., FizzBuzz, Palindrome).

Use coding platforms like LeetCode, HackerRank, or Codewars.

Practice algorithm types: sorting, searching, string manipulation, recursion.
