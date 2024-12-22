N, M = map(int, input().split())

integers = list(map(int, input().split()))

result = 1
for v in integers:
    result = ((result % M) * (v % M)) % M

print(result)