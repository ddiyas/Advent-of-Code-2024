with open("Day 4\input.txt") as file:
    letters = [list(line.strip()) for line in file]

xmas_count = 0
directions = [(-1, 1), (1, 1)]
visited = set()

for i in range(len(letters)):
    for j in range(len(letters[i])):
        if letters[i][j] == "A" and (i, j) not in visited:
            match = True
            for x, y in directions:
                ni, nj = i + x, j + y
                pi, pj = i - x, j - y
                if (
                    0 <= ni < len(letters)
                    and 0 <= nj < len(letters[i])
                    and 0 <= pi < len(letters)
                    and 0 <= pj < len(letters[i])
                    and letters[ni][nj] in {"M", "S"}
                    and letters[pi][pj] in {"M", "S"}
                    and letters[ni][nj] != letters[pi][pj]
                ):
                    continue
                else:
                    match = False
                    break

            if match:
                xmas_count += 1
                visited.add((i, j))
                for x, y in directions:
                    visited.add((i + x, j + y))
                    visited.add((i - x, j - y))

print(xmas_count)
