towers = []
pleasure = 0

N = int(input())
towers.append(N)

while towers:
    A = towers.pop()
    B = A // 2
    C = A - B

    pleasure += B * C
    towers.append(B)
    towers.append(C)

    towers = [v for v in towers if v != 1 and v != 0]

print(pleasure)