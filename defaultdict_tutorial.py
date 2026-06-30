from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())

for i in range(1, n + 1):
    word = input()
    d[word].append(str(i))

for _ in range(m):
    word = input()
    if word in d:
        print(' '.join(d[word]))
    else:
        print(-1)