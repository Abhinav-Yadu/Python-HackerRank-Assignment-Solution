K = int(input())
rooms = list(map(int, input().split()))

for room in set(rooms):
    if rooms.count(room) == 1:
        print(room)
        break