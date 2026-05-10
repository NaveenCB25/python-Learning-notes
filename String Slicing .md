# String Slicing in Python

# What is String Slicing?

## Definition

String slicing is the process of extracting a specific portion of a string.

Instead of accessing only one character using indexing, slicing allows us to get:
- Multiple characters
- A word
- A part of the string
- Even the whole string

Slicing is very useful when working with:
- User names
- Passwords
- Text processing
- Data cleaning
- Searching specific parts of text

---

# String Indexing Review

Every character in a string has an index position.

## Example

```python
text = "Hello world"
```

| Character | H | e | l | l | o |   | w | o | r | l | d |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |

---

# Basic Slicing Syntax

```python
string[start:stop]
```

---

# Understanding Start and Stop

| Part | Meaning |
|---|---|
| start | Starting index |
| stop | Ending index (not included) |

---

# Example 1

```python
text = "Hello world"

print(text[1:4])
```

## Output

```bash
ell
```

---

# Explanation

Python starts from:
- Index `1` → `e`

Stops before:
- Index `4`

Characters extracted:
- `e`
- `l`
- `l`

---

# Important Rule

## Stop Index is Non-Inclusive

This means:
- Python does NOT include the stop index character.

Example:

```python
text[1:4]
```

Includes:
- 1
- 2
- 3

Does NOT include:
- 4

---

# Omitting Start Index

## Definition

If start index is missing, Python automatically starts from `0`.

---

## Example

```python
text = "Hello world"

print(text[:5])
```

## Output

```bash
Hello
```

---

# Explanation

Python understands:

```python
text[0:5]
```

---

# Omitting Stop Index

## Definition

If stop index is missing, slicing continues until the end of the string.

---

## Example

```python
text = "Hello world"

print(text[6:])
```

## Output

```bash
world
```

---

# Explanation

Python extracts:
- Starting from index `6`
- Until the end

---

# Omitting Both Start and Stop

## Definition

If both are omitted, Python returns the entire string.

---

## Example

```python
text = "Hello world"

print(text[:])
```

## Output

```bash
Hello world
```

---

# Step Parameter in Slicing

## Definition

The step parameter controls:
- How many positions Python moves each time.

---

# Syntax with Step

```python
string[start:stop:step]
```

---

# Example 1 — Every Second Character

```python
text = "Hello world"

print(text[0:11:2])
```

## Output

```bash
Hlowrd
```

---

# Explanation

Python skips every second character.

Indexes used:
- 0 → H
- 2 → l
- 4 → o
- 6 → w
- 8 → r
- 10 → d

---

# Example 2 — Every Third Character

```python
text = "Programming"

print(text[0:11:3])
```

## Output

```bash
Pgmn
```

---

# Negative Step

## Definition

A negative step moves backward through the string.

---

# Reversing a String

## Example

```python
text = "Hello world"

print(text[::-1])
```

## Output

```bash
dlrow olleH
```

---

# Explanation

Here:
- Start is empty
- Stop is empty
- Step is `-1`

Python starts from the end and moves backward.

---

# Another Reverse Example

```python
name = "Naveen"

print(name[::-1])
```

## Output

```bash
neevaN
```

---

# Slicing Does Not Change Original String

## Definition

Slicing creates a new string.

The original string remains unchanged.

---

## Example

```python
text = "Python"

print(text[0:3])
print(text)
```

## Output

```bash
Pyt
Python
```

---

# Real-Life Example

## Extract Domain Name

```python
email = "naveen@gmail.com"

print(email[7:])
```

## Output

```bash
gmail.com
```

---

# Extract First Name

```python
full_name = "Naveen CB"

print(full_name[0:7])
```

## Output

```bash
Naveen
```

---

# Common Uses of String Slicing

String slicing is commonly used for:
- Extracting words
- Reversing strings
- Password masking
- Text formatting
- Data cleaning
- Searching specific text

---

# Important Points

- Slicing extracts part of a string
- Syntax: `[start:stop]`
- Stop index is NOT included
- Default start index is `0`
- Default stop index is end of string
- Step controls movement between indexes
- Negative step reverses string
- Slicing does not modify original string