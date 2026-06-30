import re

# Read the number of test cases
T = int(input())


float_regex = r"^[+-]?[0-9]*\.[0-9]+$"

for _ in range(T):
    string = input()
    # re.match returns a match object if valid, or None if invalid
    if re.match(float_regex, string):
        print(True)
    else:
        print(False)