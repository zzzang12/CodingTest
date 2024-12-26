import sys
input = sys.stdin.readline

N, K = map(int, input().split())
max_dists = list()
for _ in range(N):
    input()
    land = list(map(int, input().split()))
    points = [(land[i], land[i + 1]) for i in range(0, len(land), 2)]
    dists = [(v[0] ** 2 + v[1] ** 2) ** (1 / 2) for v in points]
    max_dists.append(max(dists))

max_dists.sort()
print(f'{max_dists[K - 1] ** 2:.2f}')