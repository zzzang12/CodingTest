participants = []

N = int(input())
for i in range(N):
    S, C, L = map(int, input().split())
    participant = {'index': i + 1, 'score': S, 'tries': C, 'time': L}
    participants.append(participant)

participants.sort(key=lambda x: (-x['score'], x['tries'], x['time']))

print(participants[0]['index'])