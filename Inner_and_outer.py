import re

# Read the input string
S = input()

# If a match is found, print the captured character from group 1, otherwise print -1
if m:
    print(m.group(1))
else:
    print(-1)