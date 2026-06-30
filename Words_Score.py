import re

S = input()
k = input()

pattern = rf"(?=({re.escape(k)}))"

matches = list(re.finditer(pattern, S))

if not matches:
    print((-1, -1))
else:
    for match in matches:
        
        start_idx = match.start()
        end_idx = start_idx + len(k) - 1
        print((start_idx, end_idx))