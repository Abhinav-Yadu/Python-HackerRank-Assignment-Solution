from collections import namedtuple

n = int(input())
fields = input().split()

Student = namedtuple('Student', fields)

total = 0

for _ in range(n):
    s = Student(*input().split())
    total += int(s.MARKS)

print(f"{total / n:.2f}")