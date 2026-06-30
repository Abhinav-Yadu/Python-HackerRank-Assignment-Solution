# Read the input string
S = input()

# Sort the string using a custom key tuple to prioritize groupings
sorted_chars = sorted(S, key=lambda char: (
    char.isdigit(),              
    char.isdigit() and int(char) % 2 == 0,  
    char.isupper(),              
    char                        
))

# Join the sorted characters array back into a single string and print
print("".join(sorted_chars))