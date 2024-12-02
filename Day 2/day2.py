with open("Day 2\input.txt") as file:
    reports = [list(map(int, line.split())) for line in file]

safe = 0

for level in reports:
    for i in range (1, len(level)):
        diff = level[i - 1] - level[i]
        is_safe = True
        if abs(diff) < 1 or abs(diff) > 3 or (level[0] - level[1]) * diff < 0:
            is_safe = False
            break
    if is_safe:
        safe+=1

print(safe)