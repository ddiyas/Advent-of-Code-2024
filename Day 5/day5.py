rules = {}

with open("Day 5\input_rules.txt") as file:
    for a, b in (map(int, line.strip().split("|")) for line in file):
        if a not in rules:
            rules[a] = []
        rules[a].append(b)

sum = 0
with open("Day 5\input_pages.txt") as file:
    for line in file:
        pages = list(map(int, list(line.split(","))))
        corrected = False

        while True:
            valid = True
            for i, page in enumerate(pages):
                for n in rules.get(page, []):
                    if n in pages[:i]:
                        corrected = True
                        valid = False
                        pages[i], pages[pages.index(n)] = (
                            pages[pages.index(n)],
                            pages[i],
                        )
            if valid:
                break

        if corrected:
            sum += pages[len(pages) // 2]

print(sum)
