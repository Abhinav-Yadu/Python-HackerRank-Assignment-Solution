input()
A = set(map(int, input().split()))

input()
B = set(map(int, input().split()))

for x in sorted(A.symmetric_difference(B)):
    print(x)