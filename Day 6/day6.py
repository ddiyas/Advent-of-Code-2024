with open("Day 6\input.txt") as file:
    grid = [list(line.strip()) for line in file]

guard_position = ()
marked = [[False] * len(row) for row in grid]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "^":
            guard_position = (i, j)
            marked[i][j] = True

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
guard_direction = 0
distinct = 1
while True:
    a, b = guard_position
    i, j = directions[guard_direction % len(directions)]
    if 0 <= a + i < len(grid) and 0 <= b + j < len(grid[a]):
        if grid[a + i][b + j] == "#":
            guard_direction += 1
        else:
            guard_position = (a + i, b + j)
            if not marked[a + i][b + j]:
                distinct += 1
                marked[a + i][b + j] = True
    else:
        break

print(distinct)
