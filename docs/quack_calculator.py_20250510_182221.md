# Quack Docs — calculator.py

file: calculator.py
created at: 2025-05-10
---

# Calculator Documentation

## Overview
The Calculator class is a simple arithmetic calculator that provides basic mathematical operations and maintains a memory of the last calculation result.

## Constructor
The constructor initializes a new Calculator instance with a memory value set to 0.

## Properties
• memory: Stores the result of the most recent calculation. Initialized to 0 when the calculator is created.

## Methods

### add(a, b)
Performs addition of two numbers and stores the result in memory.

Parameters:
• a: First number to add
• b: Second number to add

Returns:
• The sum of the two numbers

Example usage:

```python
calc = Calculator()
sum_result = calc.add(5, 3)  # Returns 8 and stores 8 in memory
```