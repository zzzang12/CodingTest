import sys

n1, n2 = map(int, sys.stdin.readline().split())
str1 = list(sys.stdin.readline().strip())
str2 = list(sys.stdin.readline().strip())
t = int(sys.stdin.readline())

t = min(len(str1) + len(str2) - 1, t)
str1.reverse()
str1 = list(" ".join(str1))
str2 = list(" ".join(str2))
result = list(" " * (2 * len(str1) + len(str2)))

for i, v in enumerate(str1):
    result[t * 2 + i] = v
for i, v in enumerate(str2):
    if v != " ":
        result[len(str1) + i] = v

result = "".join(result).replace(" ", "")
print(result)