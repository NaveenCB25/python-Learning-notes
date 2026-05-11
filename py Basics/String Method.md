# Common String Methods in Python

# What are String Methods?

## Definition

String methods are built-in functions provided by Python to perform operations on strings.

They help us:
- Modify text
- Search text
- Convert text
- Split text
- Format text

String methods make text handling easier and faster.

---

# Important Note

String methods do not change the original string.

They return a new modified string.

---

# 1. upper()

## Definition

The `upper()` method converts all characters in a string into uppercase letters.

---

## Syntax

```python
string.upper()
```

---

## Example

```python
text = "hello world"

result = text.upper()

print(result)
```

## Output

```bash
HELLO WORLD
```
---

# Real-Life Use

Used for:
- Login systems
- Case-insensitive comparisons
- Formatting headings

---

# 2. lower()

## Definition

The `lower()` method converts all characters into lowercase letters.

---

## Example

```python
text = "HELLO WORLD"

result = text.lower()

print(result)
```

## Output

```bash
hello world
```
---

# Real-Life Use

Used for:
- Email validation
- Username checking
- Search operations

---

# 3. strip()

## Definition

The `strip()` method removes spaces or unwanted characters from:
- Beginning
- End

of a string.

---

## Example

```python
text = "   hello world   "

result = text.strip()

print(result)
```

## Output

```bash
hello world
```
---

# Why strip() is Important

Sometimes user input contains extra spaces.

`strip()` helps clean the text.

---

# 4. replace()

## Definition

The `replace()` method replaces one part of a string with another.

---

## Syntax

```python
string.replace(old, new)
```

---

## Example

```python
text = "hello world"

result = text.replace("hello", "hi")

print(result)
```

## Output

```bash
hi world
```
---

# Another Example

```python
message = "I like Java"

new_message = message.replace("Java", "Python")

print(new_message)
```

## Output

```bash
I like Python
```

---

# 5. split()

## Definition

The `split()` method divides a string into a list.

By default, it splits using spaces.

---

## Example

```python
text = "hello world"

result = text.split()

print(result)
```

## Output

```bash
['hello', 'world']
```

---

# Split Using Separator

## Example

```python
data = "apple,banana,mango"

result = data.split(",")

print(result)
```

## Output

```bash
['apple', 'banana', 'mango']
```

---

# 6. join()

## Definition

The `join()` method combines list elements into a single string.
---

## Example

```python
words = ["hello", "world"]

result = " ".join(words)

print(result)
```

## Output

```bash
hello world
```

---

# Another Example

```python
letters = ["P", "Y", "T", "H", "O", "N"]

result = "-".join(letters)

print(result)
```

## Output

```bash
P-Y-T-H-O-N
```

---

# 7. startswith()

## Definition

Checks whether a string starts with a specific word or character.

Returns:
- True
- False

---

## Example

```python
text = "hello world"

print(text.startswith("hello"))
```

## Output

```bash
True
```
---

# 8. endswith()

## Definition

Checks whether a string ends with a specific word or character.

---

## Example

```python
text = "hello world"

print(text.endswith("world"))
```

## Output

```bash
True
```

---

# 9. find()

## Definition

The `find()` method returns the index position of the first occurrence of a substring.

If not found, it returns `-1`.

---

## Example

```python
text = "hello world"

print(text.find("world"))
```

## Output

```bash
6
```

---

# Example When Not Found

```python
text = "hello world"

print(text.find("python"))
```

## Output

```bash
-1
```

---

# 10. count()

## Definition

The `count()` method counts how many times a character or word appears.

---

## Example

```python
text = "hello world"

print(text.count("o"))
```

## Output

```bash
2
```

---

# Another Example

```python
text = "banana"

print(text.count("a"))
```

## Output

```bash
3
```

---

# 11. capitalize()

## Definition

The `capitalize()` method converts:
- First letter → uppercase
- Remaining letters → lowercase

---

## Example

```python
text = "hello world"

print(text.capitalize())
```

## Output

```bash
Hello world
```

---

# 12. isupper()

## Definition

Checks whether all letters are uppercase.

Returns:
- True
- False

---

## Example

```python
text = "HELLO"

print(text.isupper())
```

## Output

```bash
True
```

---

# 13. islower()

## Definition

Checks whether all letters are lowercase.

---

## Example

```python
text = "hello"

print(text.islower())
```

## Output

```bash
True
```

---

# 14. title()

## Definition

The `title()` method converts the first letter of every word into uppercase.

---

## Example

```python
text = "hello world"

print(text.title())
```

## Output

```bash
Hello World
```

---

# Real-Life Example Program

```python
name = "   naveen cb   "

print(name.strip())
print(name.upper())
print(name.title())
```

## Output

```bash
naveen cb
NAVEEN CB
Naveen Cb
```

---

# Summary Table

| Method | Purpose |
|---|---|
| upper() | Convert to uppercase |
| lower() | Convert to lowercase |
| strip() | Remove spaces |
| replace() | Replace text |
| split() | Split string |
| join() | Join list into string |
| startswith() | Check starting text |
| endswith() | Check ending text |
| find() | Find index |
| count() | Count occurrences |
| capitalize() | Capitalize first letter |
| isupper() | Check uppercase |
| islower() | Check lowercase |
| title() | Capitalize every word |

---

# Important Points

- String methods help manipulate text
- Methods return new strings
- Original string remains unchanged
- `split()` creates lists
- `join()` combines lists
- `find()` returns `-1` if not found
- `count()` counts occurrences
- `upper()` and `lower()` change text case