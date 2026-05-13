# --- 1. DATA TYPES (STRINGS) ---
# We use single or double quotes to tell Python this is text data.
first_name = 'John'
last_name = 'Doe'

# --- 2. STRING CONCATENATION ---
# The '+' operator 'glues' strings together. 
# We manually add ' ' so the names don't touch (JohnDoe vs John Doe).
full_name = first_name + ' ' + last_name

# --- 3. MUTABILITY & AUGMENTED ASSIGNMENT ---
# Strings are 'immutable' (cannot be changed), so '+=' actually 
# creates a brand new string and replaces the old 'address' variable.
address = '123 Main Street'
address += ', Apartment 4B' # Shorthand for: address = address + ', Apartment 4B'

# --- 4. DATA TYPES (INTEGERS) ---
# Numbers used for math or data storage do NOT get quotes.
employee_age = 28
salary = 75000 

# --- 5. STRING LITERALS ---
# This is just a plain piece of text stored in a variable name.
position = 'Data Analyst'

# --- 6. F-STRINGS (FORMATTED STRING LITERALS) ---
# The most powerful way to combine data. 
# 1. The 'f' prefix tells Python to look for curly brackets {}.
# 2. Python evaluates (calculates) whatever is inside {} and converts it to text.
# 3. This avoids 'TypeErrors' because f-strings handle numbers automatically.

employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'

# --- 7. OUTPUT ---
# This sends the data from the computer's memory to your terminal/screen.
print(employee_card)