from sys import stdin
from collections import Counter
input = stdin.readline

input()
moves_copy = Counter(input())
dest_num = int(input())
count = 0

for _ in range(dest_num):
    moves = moves_copy.copy()
    dest = list(map(int, input().split()))
    origin = [1, 1]

    if dest[0] > origin[0] and dest[1] > origin[1] and moves['X']:
        diff = min(dest[0] - origin[0], dest[1] - origin[1], moves['X'])
        origin[0] += diff
        origin[1] += diff
        moves['X'] -= diff

    if dest[0] > origin[0] and moves['R']:
        diff = min(dest[0] - origin[0], moves['R'])
        origin[0] += diff
        moves['R'] -= diff

    if dest[1] > origin[1] and moves['U']:
        diff = min(dest[1] - origin[1], moves['U'])
        origin[1] += diff
        moves['U'] -= diff

    if dest == origin:
        count += 1

print(count)