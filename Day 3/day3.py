import re

with open("Day 3\input.txt") as file:
    input_string = file.read()

multiply = re.findall("mul\([0-9]+\,[0-9]+\)", input_string)

answer = sum(
    a * b
    for a, b in tuple(
        map(int, factor.replace("mul(", "").replace(")", "").split(","))
        for factor in multiply
    )
)

print(answer)
