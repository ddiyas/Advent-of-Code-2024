import itertools

equations = []

with open("Day 7\input.txt") as file:
    for line in file:
        split = line.strip().split(":")
        pair = (int(split[0]), list(map(int, split[1].strip().split(" "))))
        equations.append(pair)

total = 0
for pair in equations:
    e_sum, digits = pair

    operator_combinations = list(
        itertools.product([True, False], repeat=len(digits) - 1)
    )
    for combination in operator_combinations:
        running_sum = digits[0]
        for i in range(1, len(digits)):
            if combination[i - 1]:
                running_sum += digits[i]
            else:
                running_sum = running_sum * digits[i]
            if running_sum > e_sum:
                break
        if running_sum == e_sum:
            total += e_sum
            break

print(total)
