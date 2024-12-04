import re

with open("Day 3\input.txt") as file:
    input_string = file.read()

multiply = re.findall("mul\([0-9]+\,[0-9]+\)|do\(\)|don't\(\)", input_string)

do = True
answer = 0
for factor in multiply:
    if factor == "do()":
        do = True
    elif factor == "don't()":
        do = False
    else:
        if do:
            pair = tuple(
                map(int, factor.replace("mul(", "").replace(")", "").split(","))
            )
            answer += pair[0] * pair[1]

print(answer)
