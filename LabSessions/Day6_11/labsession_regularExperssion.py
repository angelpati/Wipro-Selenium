#Write a regex to check if a string contains only digits.

import re

text = "Hello python World HELLO world 1234567890 python PYTHON hello world"

print("1. Write a regex to check if a string contains only digits.")
print(bool(re.fullmatch(r"\d+", "123456")))

print("2. Write a pattern to match a 10-digit mobile number.")
print(re.findall(r"\b\d{10}\b", text))

print("3. Find all lowercase letters in a string.")
print(re.findall(r"[a-z]", text))

print("4. Extract all uppercase letters from a sentence.")
print(re.findall(r"[A-Z]", text))

print("5. Match a string that starts with 'Hello'.")
print(bool(re.match(r"^Hello", text)))

print("6. Match a string that ends with 'world'.")
print(bool(re.search(r"world$", text)))

print("7. Find all words separated by spaces.")
print(re.findall(r"\S+", text))

print("8. Match exactly 5 characters.")
print(re.findall(r"\b\w{5}\b", text))

print("9. Find all occurrences of the word 'python' (case-sensitive).")
print(re.findall(r"\bpython\b", text,re.IGNORECASE))

print("10. Replace all spaces in a string with underscores.")
print(re.sub(r"\s", "_", text))

#Write a pattern to match a 10-digit mobile number.
#Find all lowercase letters in a string.
#Extract all uppercase letters from a sentence.
#Match a string that starts with "Hello".
#Match a string that ends with "world".
#Find all words separated by spaces.
#Match exactly 5 characters.
#Find all occurrences of the word "python" (case-sensitive).
#Replace all spaces in a string with underscores.