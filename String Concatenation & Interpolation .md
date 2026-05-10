# String Concatenation and String Interpolation in Python

# What is String Concatenation?

## Definition

String concatenation is the process of joining two or more strings together.

Python uses the plus operator `+` to combine strings.

Concatenation helps combine:
- Names
- Messages
- Sentences
- User input
- Dynamic text

---

# Basic String Concatenation

## Syntax

```python
string1 + string2
```

---

## Example 1

```python
first_name = "Naveen"
last_name = "CB"

full_name = first_name + last_name

print(full_name)
```

## Output

```bash
NaveenCB
```

Notice:
- No space is added automatically.

---

# Adding Space Between Strings

## Example 2

```python
first_name = "Naveen"
last_name = "CB"

full_name = first_name + " " + last_name

print(full_name)
```

## Output

```bash
Naveen CB
```

---

# Concatenating Multiple Strings

## Example

```python
greeting = "Hello"
name = "Naveen"
city = "Harihar"

message = greeting + " " + name + " from " + city

print(message)
```

## Output

```bash
Hello Naveen from Harihar
```

---

# Concatenating String and Integer

## Problem

Python cannot directly combine:
- String (`str`)
- Integer (`int`)

---

## Wrong Example

```python
name = "Naveen"
age = 20

result = name + age

print(result)
```

## Output

```bash
TypeError
```

---

# Why Error Happens

Python only allows concatenation between strings.

The variable `age` is an integer, not a string.

---

# str() Function

## Definition

The `str()` function converts other data types into strings.

---

## Correct Example

```python
name = "Naveen"
age = 20

result = name + str(age)

print(result)
```

## Output

```bash
Naveen20
```

---

# Adding Better Formatting

## Example

```python
name = "Naveen"
age = 20

result = name + " is " + str(age) + " years old"

print(result)
```

## Output

```bash
Naveen is 20 years old
```

---

# Augmented Assignment Operator (`+=`)

## Definition

The `+=` operator combines:
- Concatenation
- Assignment

in a single step.

---

## Example

```python
message = "Hello"

message += " World"

print(message)
```

## Output

```bash
Hello World
```

---

# Another Example

```python
name = "Naveen"

name += " CB"

print(name)
```

## Output

```bash
Naveen CB
```

---

# What is String Interpolation?

## Definition

String interpolation means inserting variables or expressions inside a string.

Python mainly uses:
- f-strings

for interpolation.

---

# What are f-Strings?

## Definition

F-strings are formatted strings introduced with:
- `f`
- `F`

before the string quotes.

They allow variables and expressions inside curly braces `{}`.

---

# Basic f-String Syntax

```python
f"text {variable}"
```

---

# Example 1

```python
name = "Naveen"
age = 20

message = f"My name is {name} and I am {age} years old"

print(message)
```

## Output

```bash
My name is Naveen and I am 20 years old
```

---

# Why f-Strings Are Better

Advantages:
- Easy to read
- Cleaner syntax
- No need for `str()`
- Faster and modern method

---

# Using Expressions Inside f-Strings

## Example

```python
num1 = 5
num2 = 10

print(f"The sum is {num1 + num2}")
```

## Output

```bash
The sum is 15
```

---

# More Examples

## Example 1

```python
city = "Harihar"

print(f"I live in {city}")
```

## Output

```bash
I live in Harihar
```

---

## Example 2

```python
language = "Python"
version = 3

print(f"{language} version is {version}")
```

## Output

```bash
Python version is 3
```

---

# Concatenation vs Interpolation

| Concatenation | Interpolation |
|---|---|
| Uses `+` operator | Uses f-strings |
| Requires `str()` conversion | Converts automatically |
| Harder to read | Easy to read |
| Older method | Modern method |

---

# Real-Life Example

## Concatenation

```python
name = "Naveen"
course = "Python"

print(name + " is learning " + course)
```

---

## f-String

```python
name = "Naveen"
course = "Python"

print(f"{name} is learning {course}")
```

---

# Important Points

- Concatenation joins strings
- `+` operator combines strings
- `str()` converts values into strings
- `+=` appends strings
- f-strings are used for interpolation
- f-strings use `{}` brackets
- f-strings automatically convert data types
- f-strings are cleaner and easier to read