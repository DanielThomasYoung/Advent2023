from functools import lru_cache


def main():
    ONE_BILLION = 1000000000
    previous_lists = []
    with open("day14.txt", "r") as file:
        lines = [list(line.strip()) for line in file]
    lines_clone = lines[:]

    previous_lists = []
    repeat_count = 1

    for index in range(ONE_BILLION):
        lines = cycle(lines)

        if lines in previous_lists:
            repeat_count = index - previous_lists.index(lines)
            break

        previous_lists.append(lines)

    for _ in range(ONE_BILLION % repeat_count + repeat_count):
        lines_clone = cycle(lines_clone)

    print(find_final_sum(lines_clone))


def cycle(lines):
    north = list(map(list, zip(*lines)))
    roll(north)
    west = list(map(list, zip(*north)))
    roll(west)
    south = [row[::-1] for row in list(map(list, zip(*west)))]
    roll(south)
    east = [row[::-1] for row in list(map(list, zip(*south)))]
    roll(east)
    return [row[::-1] for row in reversed(east)]


def roll(lines):
    for line_index in range(len(lines)):
        latest_square = -1

        for index in range(len(lines[0])):
            char = lines[line_index][index]
            if char == "O":
                latest_square += 1
                lines[line_index][index] = "."
                lines[line_index][latest_square] = "O"
            elif char == "#":
                latest_square = index


def find_final_sum(lines):
    total_sum = 0
    transposed = [row[::-1] for row in list(map(list, zip(*lines)))]
    for line in transposed:
        for index in range(len(line)):
            if line[index] == "O":
                total_sum += index + 1

    return total_sum


if __name__ == "__main__":
    main()
