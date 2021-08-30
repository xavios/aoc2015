import os


def santa(instr):
    level = 0
    for step in instr:
        if step == "(":
            level = level + 1
        elif step == ")":
            level = level - 1
    return level


assert santa("(())") == 0
assert santa("()()") == 0
assert santa("(((") == 3
assert santa(")())())") == -3

# second part


def basementLevel(instr):
    level = 0
    at_step = 0
    for step in instr:
        at_step = at_step + 1
        if step == "(":
            level = level + 1
        elif step == ")":
            level = level - 1
        if level == -1:
            return at_step


assert basementLevel("()())") == 5

input = open(r"01-1.txt", "r")
input = input.readline()

print(santa(input))
print(basementLevel(input))
