from functools import reduce

data = [("Ania", 82), ("Bartek", 91), ("Celina", 67), ("Darek", 78)]

average = lambda scores: reduce(lambda acc, x: acc + x, scores) / len(scores)

scores_over_70 = list(map(lambda x: x[1], filter(lambda x: x[1] > 70, data)))

print("Średnia:", round(average(scores_over_70), 2))
