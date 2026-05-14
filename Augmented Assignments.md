# Augmented Assignments in Python

# What is Augmented Assignment?

## Definition

Augmented assignment is a shortcut way of:
- Performing an operation
- Updating the same variable

in a single step.

Instead of writing:

```python
x = x + 5
```

Python provides a shorter and cleaner form:

```python
x += 5
```

This is called:
- Augmented assignment

---

# Why Augmented Assignments are Important

Augmented assignments help:
- Reduce code length
- Improve readability
- Avoid repeating variable names
- Make calculations easier

They are commonly used in:
- Counters
- Loops
- Calculators
- Games
- Banking systems

---

# Basic Syntax

```python
variable operator= value
```

---

# Normal Assignment vs Augmented Assignment

| Normal Assignment | Augmented Assignment |
|---|---|
| `x = x + 5` | `x += 5` |
| `x = x - 2` | `x -= 2` |
| `x = x * 3` | `x *= 3` |

---

# Addition Assignment (`+=`)

## Definition

Adds a value to the variable and stores the result back into the same variable.

---

## Example

```python
count = 10

count += 5

print(count)
```

## Output

```bash
15
```

---

# Step-by-Step Explanation

Initially:

```python
count = 10
```

Then:

```python
count += 5
```

means:

```python
count = count + 5
```

Result:
- 10 + 5 = 15

---

# Real-Life Example

```python
wallet = 500

wallet += 200

print(wallet)
```

## Output

```bash
700
```

Explanation:
- ₹200 added to wallet balance.

---

# Subtraction Assignment (`-=`)

## Definition

Subtracts a value from the variable and stores the updated result.

---

## Example

```python
marks = 95

marks -= 10

print(marks)
```

## Output

```bash
85
```

---

# Real-Life Example

```python
battery = 100

battery -= 20

print(battery)
```

## Output

```bash
80
```

Explanation:
- Battery reduced by 20%.

---

# Multiplication Assignment (`*=`)

## Definition

Multiplies the variable by another value and stores the result.

---

## Example

```python
price = 50

price *= 4

print(price)
```

## Output

```bash
200
```

---

# Real-Life Example

```python
salary = 10000

salary *= 2

print(salary)
```

## Output

```bash
20000
```

Explanation:
- Salary doubled.

---

# Division Assignment (`/=`)

## Definition

Divides the variable by another value and stores the result.

---

## Example

```python
money = 100

money /= 4

print(money)
```

## Output

```bash
25.0
```

---

# Why Result is Float?

Division in Python always returns a float value.

---

# Floor Division Assignment (`//=`)

## Definition

Divides the value and removes the decimal part.

---

## Example

```python
pages = 23

pages //= 5

print(pages)
```

## Output

```bash
4
```

---

# Explanation

23 ÷ 5 = 4.6

Floor division removes decimal:
- Result becomes `4`

---

# Modulo Assignment (`%=`)

## Definition

Stores the remainder after division.

---

## Example

```python
number = 35

number %= 2

print(number)
```

## Output

```bash
1
```

---

# Real-Life Use

Used for:
- Even/odd checking
- Game scores
- Time calculations

---

# Exponentiation Assignment (`**=`)

## Definition

Raises a number to a power and stores the result.

---

## Example

```python
power = 2

power **= 3

print(power)
```

## Output

```bash
8
```

---

# Explanation

```python
2 ** 3
```

means:

```python
2 × 2 × 2 = 8
```

---

# Augmented Assignment with Strings

Some augmented assignments work with strings.

---

# String Concatenation Using `+=`

## Example

```python
greet = "Hello"

greet += " World"

print(greet)
```

## Output

```bash
Hello World
```

---

# Explanation

Python combines:
- `"Hello"`
- `" World"`

into one string.

---

# String Repetition Using `*=`

## Example

```python
text = "Hi "

text *= 3

print(text)
```

## Output

```bash
Hi Hi Hi
```

---

# Invalid String Operations

Some operators do not work with strings.

---

# Example

```python
text = "Hello"

text -= "World"
```

## Output

```bash
TypeError
```

---

# Why Error Happens

Python does not support:
- subtraction
- division

for strings.

Strings only support:
- concatenation
- repetition

---

# Increment and Decrement Operators

In some languages:
- `++`
- `--`

increase or decrease values.

Python does NOT support them.

---

# Wrong Example

```python
x++
```

This gives an error in Python.

---

# Correct Python Way

```python
x += 1
```

---

# Example

```python
x = 5

x += 1

print(x)
```

## Output

```bash
6
```

---

# What Happens with `++x`?

Python treats:
- `++x`

as:
- positive sign applied twice

It does NOT increment the value.

---

# Example

```python
x = 5

print(+x)
print(++x)
print(+++x)
```

## Output

```bash
5
5
5
```

---

# Real-Life Counter Example

```python
likes = 0

likes += 1
likes += 1
likes += 1

print(likes)
```

## Output

```bash
3
```

---

# Banking Example

```python
balance = 1000

balance += 500
balance -= 200

print(balance)
```

## Output

```bash
1300
```

---

# Important Points

- Augmented assignment updates variables quickly
- `+=` adds values
- `-=` subtracts values
- `*=` multiplies values
- `/=` divides values
- `%=` stores remainder
- `**=` performs exponentiation
- `//=` removes decimal values
- Strings support `+=` and `*=`
- Python does not support `++` or `--`