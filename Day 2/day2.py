def is_safe(level):
    for i in range(1, len(level)):
        diff = level[i - 1] - level[i]
        is_safe = True
        if abs(diff) < 1 or abs(diff) > 3 or (level[0] - level[1]) * diff < 0:
            return False
    return True


with open("Day 2\input.txt") as file:
    reports = [list(map(int, line.split())) for line in file]

safe = 0

for level in reports:
    if is_safe(level):
        safe += 1
    else:
        for i in range(0, len(level)):
            new_level = level[:i] + level[i + 1 :]
            if is_safe(new_level):
                safe += 1
                break

print(safe)
