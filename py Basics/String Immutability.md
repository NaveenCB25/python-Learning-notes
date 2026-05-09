# Strings and String Immutability in Python

# What is a String?

A string is a data type used to store text in Python.

A string is made up of a sequence of characters such as:
- Letters
- Numbers
- Symbols
- Spaces

Strings are written inside:
- Single quotes `' '`
- Double quotes `" "`

Python treats both single and double quotes the same way.

---

# Why Strings Are Important

Strings are used everywhere in programming.

They help store:
- Names
- Messages
- Passwords
- User input
- Addresses
- Text data

Without strings, handling text in programs would not be possible.

---

# Creating Strings

## Using Double Quotes

```python
name = "Naveen"

print(name)
```

## Output

```bash
Naveen
```

---

## Using Single Quotes

```python
city = 'Harihar'

print(city)
```

## Output

```bash
Harihar
```

---

# Multi-line Strings

## Definition

Multi-line strings allow text to span across multiple lines.

Python uses:
- Triple double quotes `""" """`
- Triple single quotes `''' '''`

---

## Example

```python
message = """Welcome
to
Python"""

print(message)
```

## Output

```bash
Welcome
to
Python
```

---

# Quotes Inside Strings

Sometimes strings contain quotation marks.

Python provides two ways to handle this.

---

# Method 1: Use Opposite Quotes

If the text contains single quotes, use double quotes outside.

## Example

```python
msg = "It's a sunny day"

print(msg)
```

## Output

```bash
It's a sunny day
```

---

## Another Example

```python
quote = 'She said, "Hello"'

print(quote)
```

## Output

```bash
She said, "Hello"
```

---

# Method 2: Escape Characters

## Definition

An escape character (`\`) tells Python to ignore the special meaning of a character.

---

## Example

```python
msg = 'It\'s raining'

print(msg)
```

## Output

```bash
It's raining
```

---

# Checking Text Inside a String

## Definition

Python uses the `in` operator to check whether a word or character exists inside a string.

It returns:
- `True`
- `False`

---

## Example

```python
text = "Hello world"

print("Hello" in text)
print("Python" in text)
```

## Output

```bash
True
False
```

---

# String Length

## Definition

The `len()` function returns the total number of characters in a string.

Spaces are also counted.

---

## Example

```python
text = "Hello world"

print(len(text))
```

## Output

```bash
11
```

---

# String Indexing

## Definition

Each character in a string has a position number called an index.

Indexing starts from `0`.

---

# Index Table Example

| Character | P | y | t | h | o | n |
|---|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 |

---

## Example

```python
text = "Python"

print(text[0])
print(text[1])
print(text[5])
```

## Output

```bash
P
y
n
```

---

# Negative Indexing

## Definition

Negative indexing starts counting from the end.

| Character | P | y | t | h | o | n |
|---|---|---|---|---|---|---|
| Negative Index | -6 | -5 | -4 | -3 | -2 | -1 |

---

## Example

```python
text = "Python"

print(text[-1])
print(text[-2])
```

## Output

```bash
n
o
```

---

# What is String Immutability?

## Definition

Strings in Python are immutable.

Immutable means:
- The original string cannot be changed after creation.

You cannot:
- Replace characters
- Remove characters
- Modify characters directly

---

# Why Strings Are Immutable

Python makes strings immutable for:
- Better memory management
- Faster performance
- Improved security
- Data safety

---

# Reassigning a String

You cannot modify a string directly,
but you can assign a completely new string.

---

## Example

```python
greeting = "Hi"

greeting = "Hello"

print(greeting)
```

## Output

```bash
Hello
```

In this example:
- `"Hi"` is not modified
- Variable now points to a new string `"Hello"`

---

# Invalid String Modification

## Example

```python
text = "Python"

text[0] = "J"
```

## Output

```bash
TypeError
```

---

# Why Error Happens

Python does not allow changing characters directly because strings are immutable.

---

# Immutable Data Types in Python

These data types are immutable:
- String (`str`)
- Integer (`int`)
- Float (`float`)
- Boolean (`bool`)
- Tuple (`tuple`)
- Range (`range`)

---

# Mutable vs Immutable

| Mutable | Immutable |
|---|---|
| Can be changed | Cannot be changed |
| Example: List | Example: String |

---

# Important Points

- Strings store text data
- Strings use quotes
- `len()` returns string length
- Indexing starts from `0`
- Negative indexing starts from `-1`
- `in` operator checks text existence
- Strings are immutable
- Direct modification is not allowed
- Reassignment is allowed