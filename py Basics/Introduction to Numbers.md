# Integers and Floating Point Numbers in Python

# Introduction to Numbers in Python

Numbers are one of the most important parts of programming.

In Python, numbers help us:
- Perform calculations
- Store marks and salaries
- Calculate prices
- Measure height and weight
- Build calculators
- Create banking and shopping applications

Python mainly uses two numeric data types:
- Integer (`int`)
- Float (`float`)

Both are used to store numeric values, but they work differently.

---

# What is an Integer?

## Definition

An integer is a whole number without any decimal point.

Integers can be:
- Positive numbers
- Negative numbers
- Zero

---

# Examples of Integers

```python
age = 21
marks = 95
temperature = -5
balance = 0
```

---

# Real-Life Examples

| Situation | Integer Example |
|---|---|
| Student age | 20 |
| Mobile OTP | 458921 |
| Number of books | 12 |
| Temperature | -2 |

---

# Integer Program Example

```python
age = 20
marks = 95

print(age)
print(marks)
```

## Output

```bash
20
95
```

---

# Integer Type Checking

Python allows us to check the type of a value using the `type()` function.

## Example

```python
number = 56

print(type(number))
```

## Output

```bash
<class 'int'>
```

This means:
- Python identifies `56` as an integer.

---

# What is a Float?

## Definition

A float is a number that contains decimal values.

Float stands for:
- Floating-point number

The decimal point can “float” to different positions.

---

# Examples of Floats

```python
price = 99.99
height = 5.8
temperature = -2.4
```

---

# Real-Life Examples

| Situation | Float Example |
|---|---|
| Product price | 199.99 |
| Height | 5.7 |
| Petrol quantity | 2.5 liters |
| Weight | 60.5 kg |

---

# Float Program Example

```python
price = 99.5
weight = 60.5

print(price)
print(weight)
```

## Output

```bash
99.5
60.5
```

---

# Float Type Checking

```python
number = 5.4

print(type(number))
```

## Output

```bash
<class 'float'>
```

Python recognizes decimal values as float data types.

---

# Difference Between Integer and Float

| Integer | Float |
|---|---|
| Whole numbers | Decimal numbers |
| No decimal point | Has decimal point |
| Example: 10 | Example: 10.5 |

---

# Arithmetic Operations in Python

Python supports mathematical calculations.

These are called:
- Arithmetic operations

---

# Common Arithmetic Operators

| Operator | Meaning |
|---|---|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Modulo |
| // | Floor Division |
| ** | Exponentiation |

---

# Addition

## Definition

Addition combines two numbers.

---

## Integer Addition

```python
num1 = 50
num2 = 20

result = num1 + num2

print(result)
```

## Output

```bash
70
```

---

## Float Addition

```python
price1 = 99.5
price2 = 50.5

total = price1 + price2

print(total)
```

## Output

```bash
150.0
```

---

# Subtraction

## Definition

Subtraction removes one number from another.

---

## Example

```python
marks = 95
lost_marks = 10

final_marks = marks - lost_marks

print(final_marks)
```

## Output

```bash
85
```

---

# Multiplication

## Definition

Multiplication repeats addition multiple times.

---

## Example

```python
price = 50
quantity = 4

total = price * quantity

print(total)
```

## Output

```bash
200
```

---

# Division

## Definition

Division splits a number into equal parts.

---

## Example

```python
money = 100
friends = 4

share = money / friends

print(share)
```

## Output

```bash
25.0
```

Notice:
- Division always returns a float in Python.

---

# Integer and Float Together

## Definition

When Python combines:
- Integer
- Float

the result automatically becomes a float.

---

## Example

```python
age = 20
height = 5.7

result = age + height

print(result)
print(type(result))
```

## Output

```bash
25.7
<class 'float'>
```

---

# Why Python Converts to Float

Python converts to float because:
- Float is more precise
- Decimal values should not be lost

---

# Modulo Operator (`%`)

## Definition

The modulo operator returns the remainder after division.

---

## Example

```python
print(10 % 3)
```

## Output

```bash
1
```

Explanation:
- 10 divided by 3 gives remainder 1.

---

# Real-Life Use of Modulo

Used for:
- Checking even or odd numbers
- Digital clocks
- Game logic

---

# Floor Division (`//`)

## Definition

Floor division removes decimal values and returns the nearest lower whole number.

---

## Example

```python
print(10 // 3)
```

## Output

```bash
3
```

---

# Exponentiation (`**`)

## Definition

Exponentiation means:
- Raising a number to a power.

---

## Example

```python
print(2 ** 3)
```

## Output

```bash
8
```

Explanation:
- 2 × 2 × 2 = 8

---

# Float Precision Problem

Sometimes float calculations show extra decimal digits.

---

## Example

```python
print(0.1 + 0.2)
```

## Output

```bash
0.30000000000000004
```

---

# Why This Happens

Computers store numbers in binary format.

Some decimal values cannot be stored perfectly.

This creates small rounding errors.

---

# Type Conversion

## Definition

Type conversion means changing one data type into another.

Python provides:
- `int()`
- `float()`

functions for conversion.

---

# float() Function

## Definition

Converts values into float type.

---

## Example

```python
num = 56

result = float(num)

print(result)
```

## Output

```bash
56.0
```

---

# int() Function

## Definition

Converts values into integer type.

---

## Example

```python
num = 12.9

result = int(num)

print(result)
```

## Output

```bash
12
```

Notice:
- Decimal part is removed.

---

# String to Number Conversion

## Example

```python
num = "45"

print(int(num))
```

## Output

```bash
45
```

---

# round() Function

## Definition

Rounds numbers to nearby values.

---

## Example

```python
print(round(4.7))
print(round(4.253, 1))
```

## Output

```bash
5
4.3
```

---

# abs() Function

## Definition

Returns the positive version of a number.

---

## Example

```python
print(abs(-10))
```

## Output

```bash
10
```

---

# pow() Function

## Definition

Raises numbers to powers.

---

## Example

```python
print(pow(2, 3))
```

## Output

```bash
8
```

---

# Real-Life Calculator Program

```python
num1 = 20
num2 = 5

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
```

---

# Important Points

- Integers store whole numbers
- Floats store decimal numbers
- Python supports arithmetic calculations
- Integer + Float returns Float
- `%` gives remainder
- `//` removes decimal part
- `**` performs exponentiation
- `int()` converts to integer
- `float()` converts to float
- `round()` rounds numbers
- `abs()` returns positive value