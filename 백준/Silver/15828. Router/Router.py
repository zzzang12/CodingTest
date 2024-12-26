from sys import stdin
from collections import deque

input = stdin.readline
router = deque()
capacity = int(input())

while True:
    packet = int(input())
    if packet == -1:
        break

    if packet == 0 and router:
        router.popleft()
        continue

    if len(router) < capacity:
        router.append(packet)

if router:
    print(*router)
else:
    print('empty')