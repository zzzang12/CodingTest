import sys

n, k = map(int, sys.stdin.readline().split())
l = [v for v in range(1, n + 1) if n % v == 0]
if len(l) < k:
    print(0)
else:
    print(l[k - 1])