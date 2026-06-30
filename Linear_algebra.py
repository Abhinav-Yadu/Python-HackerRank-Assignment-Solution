import re

# Read the input string
S = input()

consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

pattern = rf"(?<=[{consonants}])([{vowels}]{{2,}})(?=[{consonants}])"

# Find all matching vowel groups (case-insensitive flag applied just in case)
matches = re.findall(pattern, S, re.IGNORECASE)

# If matches exist, print each on a new line; otherwise, print -1
if matches:
    for match in matches:
        print(match)
else:
    print(-1)