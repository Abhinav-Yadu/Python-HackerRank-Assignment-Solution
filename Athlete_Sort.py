# Read the number of athletes (N) and attributes (M)
N, M = map(int, input().split())

# Read the table of athlete attributes
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# Read the attribute index K to sort by
K = int(input())

# Sort the array 
arr.sort(key=lambda x: x[K])

# Print the sorted rows
for row in arr:
    print(*row)