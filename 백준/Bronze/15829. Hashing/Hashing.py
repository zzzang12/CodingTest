r = 31
M = 1234567891
input()
lst = list(input())

H = 0
for i, v in enumerate(lst):
    H += ((ord(v) - 96) * (r ** i))

print(H % M)
