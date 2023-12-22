def split_list(original: list) -> list:
    sub = []
    del original[0]
    while original:
        line = original.pop(0)
        if not line:
            return sub
        sub.append(line.split())
    return sub


def adjust(inputs: list[int], mapping: list[int]):
    for map in mapping:
        int_map = [int(i) for i in map]

        for i in range(len(inputs)):
            if inputs[i] >= int_map[1] and inputs[i] < (int_map[1] + int_map[2]):
                inputs[i] += int_map[0] - int_map[1]


with open("day5test.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    seeds = lines.pop(0).split()
    del lines[0]
    del seeds[0]
    current_answer = [int(seed) for seed in seeds]

    while lines:
        maps = split_list(lines)

        adjust(current_answer, maps)

    print(min(current_answer))
