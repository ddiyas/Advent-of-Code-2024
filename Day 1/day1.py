with open("Day 1\input.txt") as file:
    pairs = [tuple(map(int, line.split())) for line in file]

ids1, ids2 = zip(*pairs)

ids1 = sorted(ids1)
ids2 = sorted(ids2)

diff_sum = sum(abs(a - b) for a, b in zip(ids1, ids2))

print(diff_sum)

similarity_score = sum(ids2.count(i) * i for i in ids1)

print(similarity_score)