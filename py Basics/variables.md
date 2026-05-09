# Python Variables

## What is a Variable?
A variable is used to store data.

Think of it like a box that stores information.

---

# Declaring Variables

## Syntax

```python
variable_name = value
```

## Example

```python
name = "John Doe"
age = 25
```

---

# Strings in Python

Strings are text values written inside quotes.

## Example

```python
city = "Harihar"
course = 'Python'
```

---

# Variable Naming Rules

## 1. Start with letter or underscore

✅ Correct

```python
user_name = "Naveen"
_age = 20
```

❌ Wrong

```python
5name = "Error"
```

---

## 2. Use letters, numbers, underscore

✅ Example

```python
student1 = "Ram"
user_age = 21
```

---

## 3. Variable names are case-sensitive

```python
age = 20
Age = 30
AGE = 40
```

All are different variables.

---

## 4. Do not use Python keywords

❌ Wrong

```python
if = 10
class = "Python"
```

---

# Naming Convention

## Use snake_case

```python
my_variable_name = "Python"
user_age = 20
```

---

# Use Meaningful Names

✅ Good

```python
user_age = 25
```

❌ Bad

```python
x = 25
ua = 25
```

---

# Comments in Python

Comments explain code.

## Single-line Comment

```python
# This is a comment
```

## Multi-line Comment

```python
# Line 1
# Line 2
# Line 3
```

---

# Example Program

```python
# User details

user_name = "Naveen"
user_age = 21

print(user_name)
print(user_age)
```

## Output

```bash
Naveen
21
```

---

# Important Points

- Python uses `=` to assign values
- No need to define data type
- Use meaningful names
- Follow snake_case
- Avoid single-letter variables
- Comments help explain code