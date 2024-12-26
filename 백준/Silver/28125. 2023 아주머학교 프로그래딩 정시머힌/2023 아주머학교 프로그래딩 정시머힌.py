table = {
    "\\\\'": 'w',
    "\\'": 'v',
    "7": 't',
    "0": 'o',
    "^": 'n',
    ";": 'j',
    "!": 'i',
    "[": 'c',
    "@": 'a'
}

N = int(input())
for _ in range(N):
    count = 0
    word = input()

    for key, value in table.items():
        while key in word:
            word = word.replace(key, value, 1)
            count += 1

    if count * 2 >= len(word):
        print("I don't understand")
    else:
        print(word)