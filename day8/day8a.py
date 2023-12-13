from time import sleep
from math import lcm
map = {
"AAA": ["BBB", "BBB"],
"BBB": ["AAA", "ZZZ"],
"ZZZ": ["ZZZ", "ZZZ"]
}

with open("day8.txt", "r") as file:
    lines = file.readlines()
    instructions = lines[0].strip()
    del(lines[0:2])

    current_keys = []
    formatted_lines = {}
    for line in lines:
        cleaned_line = line.strip().replace("=", "").replace("(", "").replace(")", "").replace(",", "").split()
        formatted_lines[cleaned_line[0]] = cleaned_line[1:3]
        if cleaned_line[0][2] == "A":
            current_keys.append(cleaned_line[0])

    end_count = []

    for key in current_keys:
        count = 0
        i = 0
        while True:
            if key[2] == "Z":
                end_count.append(count)
                break

            if instructions[i] == "L":
                key = formatted_lines[key][0]
            else:
                key = formatted_lines[key][1]

            count += 1
            i = (i + 1) % len(instructions)

    print(lcm(*end_count))
