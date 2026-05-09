# Common Data Types in Python

## What is a Data Type?

A data type defines the type of value stored in a variable.

Python automatically identifies the data type based on the assigned value.

Example:
- Number
- Text
- True or False
- Collection of items

---

# Dynamic Typing in Python

Python is a dynamically-typed language.

This means:
- No need to declare data type manually
- Python automatically understands the type

## Example

```python
name = "Naveen"
age = 20
price = 99.5
```

Python understands:
- `name` → string
- `age` → integer
- `price` → float

---

# 1. Integer (`int`)

## Definition
Integer stores whole numbers without decimal values.

## Examples

```python
age = 20
marks = 95
temperature = -5

print(age)
print(marks)
print(temperature)
```

## Output

```bash
20
95
-5
```

---

# 2. Float (`float`)

## Definition
Float stores decimal numbers.

## Examples

```python
price = 99.99
height = 5.8
weight = 60.5

print(price)
print(height)
print(weight)
```

## Output

```bash
99.99
5.8
60.5
```

---

# 3. String (`str`)

## Definition
String stores text values.

Strings are written inside:
- Single quotes `' '`
- Double quotes `" "`

## Examples

```python
name = "Naveen"
city = 'Harihar'
course = "Python"

print(name)
print(city)
print(course)
```

## Output

```bash
Naveen
Harihar
Python
```

---

# 4. Boolean (`bool`)

## Definition
Boolean stores only two values:
- True
- False

## Examples

```python
is_student = True
is_logged_in = False

print(is_student)
print(is_logged_in)
```

## Output

```bash
True
False
```

---

# 5. List (`list`)

## Definition
List stores multiple values in order.

Lists use square brackets `[]`.

## Examples

```python
numbers = [1, 2, 3, 4]
student = ["Naveen", 20, True]

print(numbers)
print(student)
```

## Output

```bash
[1, 2, 3, 4]
['Naveen', 20, True]
```

---

# 6. Tuple (`tuple`)

## Definition
Tuple stores ordered data that cannot be changed.

Tuples use parentheses `()`.

## Examples

```python
colors = ("red", "green", "blue")
marks = (90, 80, 70)

print(colors)
print(marks)
```

## Output

```bash
('red', 'green', 'blue')
(90, 80, 70)
```

---

# 7. Set (`set`)

## Definition
Set stores unique values.

Sets use curly braces `{}`.

## Examples

```python
numbers = {1, 2, 3, 4}
fruits = {"apple", "banana", "mango"}

print(numbers)
print(fruits)
```

## Output

```bash
{1, 2, 3, 4}
{'apple', 'banana', 'mango'}
```

---

# 8. Dictionary (`dict`)

## Definition
Dictionary stores data in key-value pairs.

## Examples

```python
student = {
    "name": "Naveen",
    "age": 20,
    "course": "Python"
}

print(student)
```

## Output

```bash
{'name': 'Naveen', 'age': 20, 'course': 'Python'}
```

---

# 9. Range (`range`)

## Definition
Range generates a sequence of numbers.

Mostly used in loops.

## Examples

```python
numbers = range(5)

print(numbers)
```

## Output

```bash
range(0, 5)
```

---

# 10. None (`NoneType`)

## Definition
None represents no value or empty value.

## Examples

```python
data = None

print(data)
```

## Output

```bash
None
```

---

# type() Function

## Definition
The `type()` function checks the data type of a variable.

## Examples

```python
name = "Naveen"
age = 20
price = 99.5

print(type(name))
print(type(age))
print(type(price))
```

## Output

```bash
<class 'str'>
<class 'int'>
<class 'float'>
```

---

# isinstance() Function

## Definition
The `isinstance()` function checks whether a value belongs to a specific data type.

## Examples

```python
print(isinstance(20, int))
print(isinstance("Python", str))
print(isinstance(True, bool))
```

## Output

```bash
True
True
True
```

---

# Important Points

- Python automatically detects data types
- Integer stores whole numbers
- Float stores decimal numbers
- String stores text
- Boolean stores True or False
- List stores multiple ordered values
- Dictionary stores key-value data
- `type()` checks variable type
- `isinstance()` checks data type