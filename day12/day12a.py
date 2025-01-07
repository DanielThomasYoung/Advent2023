def format_line(line):
    split_line = line.split()
    indices = find_indices(split_line[0], "?")
    data = list(split_line[0])
    targets = [int(x) for x in split_line[1].split(",")]
    return data, targets, indices


def find_indices(line, target):
    indices = []
    index = line.find(target)
    while index != -1:
        indices.append(index)
        index = line.find(target, index + 1)
    return indices


def add_to_broken(line, indices, switcher):
    cloned_line = line[:]
    for position, index in enumerate(indices):
        if switcher // (2**position) % 2:
            cloned_line[index] = "#"
    return cloned_line


def group_indices(line):
    result = []
    sum = 0
    for i in line:
        if i == "#":
            sum += 1
        elif sum:
            result.append(sum)
            sum = 0

    if sum:
        result.append(sum)
    return result


total = 0
with open("day12.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        data, targets, unknowns = format_line(line)

        for i in range(2 ** len(unknowns)):
            added_broken = add_to_broken(data, unknowns, i)
            grouped_broken = group_indices(added_broken)

            total += grouped_broken == targets

        print(f"total: {total}")
