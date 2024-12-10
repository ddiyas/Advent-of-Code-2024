with open("Day 6\input.txt") as file:
    grid = [list(line.strip()) for line in file]

marked = [[False] * len(row) for row in grid]
starting_position = ()


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "^":
            marked[i][j] = True
            starting_position = (i, j)


distinct = 1
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
guard_direction = 0
guard_position = starting_position
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


cycle_count = 0
for i in range(len(marked)):
    for j in range(len(marked[i])):
        if marked[i][j]:
            grid[i][j] = "#"
            path_length = 0
            guard_direction = 0
            guard_position = starting_position
            while True:
                a, b = guard_position
                y, z = directions[guard_direction % len(directions)]
                if 0 <= a + y < len(grid) and 0 <= b + z < len(grid[a]):
                    if grid[a + y][b + z] == "#":
                        guard_direction += 1
                    else:
                        guard_position = (a + y, b + z)
                        path_length += 1
                        if path_length > len(grid) * len(grid[i]) * 2:
                            cycle_count += 1
                            break
                else:
                    break
            grid[i][j] = "."

print(cycle_count)
