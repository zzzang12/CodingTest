testcases = int(input())
for _ in range(testcases):
  quiz = input()
  quiz = quiz.split("X")
  score = [(len(elem) * (len(elem) + 1)) // 2 for elem in quiz if len(elem) != 0]
  score = sum(score)
  print(score)