S1, S2 = map(int, input().split())

samples = [input().split() for _ in range(S1)]
samples = [v[0] == v[1] for v in samples]

if not all(samples):
    print("Wrong Answer")
    exit(0)

systems = [input().split() for _ in range(S2)]
systems = [v[0] == v[1] for v in systems]

if not all(systems):
    print("Why Wrong!!!")
    exit(0)

print("Accepted")