
_ = input()

# Read the space-separated list of integers as strings
numbers = input().split()

# Condition 1: Check if ALL elements are positive integers
condition_all_positive = all(int(x) > 0 for x in numbers)

# Condition 2: Check if ANY element is a palindromic string
condition_any_palindrome = any(x == x[::-1] for x in numbers)

# Print True if both conditions are met, otherwise print False
print(condition_all_positive and condition_any_palindrome)