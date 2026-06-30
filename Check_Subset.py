T = int(input())

for _ in range(T):
    input()
    A = set(map(int, input().split()))
    input()
    B = set(map(int, input().split()))

    if A <= B:
        print(True)
    else:
        print(False)