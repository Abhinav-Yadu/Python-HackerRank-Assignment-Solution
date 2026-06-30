# Read the main set A
A = set(map(int, input().split()))

# Read the number of other sets
n = int(input())

# Assume A is a strict superset until proven otherwise
is_strict_superset = True

for _ in range(n):
    other_set = set(map(int, input().split()))
    
    # A must be a strict superset of other_set: 
    # 1. other_set must be a subset of A (other_set.issubset(A) or other_set < A)
    # 2. A must have more elements than other_set
    if not (other_set.issubset(A) and len(A) > len(other_set)):
        is_strict_superset = False
        break  # We can stop early if any set fails the condition

print(is_strict_superset)