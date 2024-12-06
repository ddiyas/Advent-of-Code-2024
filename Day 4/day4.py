with open("Day 4\input.txt") as file:
    letters = [list(line.strip()) for line in file]

xmas_count = 0
xmas = "XMAS"
directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1)]
visited = set()

for i in range(len(letters)):
    for j in range(len(letters[i])):
        if letters[i][j] == xmas[0] and (i, j) not in visited:
            for x, y in directions:
                if all(
                    0 <= i + letter_index * x < len(letters)
                    and 0 <= j + letter_index * y < len(letters[i])
                    and letters[i + (letter_index * x)][j + (letter_index * y)]
                    == xmas[letter_index]
                    for letter_index in range(1, len(xmas))
                ):
                    xmas_count += 1
                    for k in range(len(xmas)):
                        visited.add((i + k * x, j + k * y))

print(xmas_count)
