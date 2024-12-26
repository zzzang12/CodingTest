N = int(input())
plates = list(map(int, input().split()))

tak = 0
for i in range(N - 1):
    if plates[i] >= plates[i + 1]:
        tak += 1

if plates[-1] >= plates[0]:
    tak += 1

print(tak)