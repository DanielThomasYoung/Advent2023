def main():
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    lines = []
    for line in file_lines:
        lines.append(list(line.strip()))

    positions = []
    steps = 0
    total = 0

    for line_index in range(len(lines)):
        for char_index in range(len(lines[0])):
            if lines[line_index][char_index] == "S":
                positions.append([line_index, char_index])
                lines[line_index][char_index] = "."

    while steps < 130:
        end = steps % 2
        next_positions = []
        for position in positions:
            if (
                position[1] < len(lines) - 1
                and lines[position[0]][position[1] + 1] == "."
            ):
                next_positions.append([position[0], position[1] + 1])
                if end:
                    lines[position[0]][position[1] + 1] = "O"
                    total += 1
                else:
                    lines[position[0]][position[1] + 1] = "-"
            if (
                position[0] < len(lines) - 1
                and lines[position[0] + 1][position[1]] == "."
            ):
                next_positions.append([position[0] + 1, position[1]])
                if end:
                    lines[position[0] + 1][position[1]] = "O"
                    total += 1
                else:
                    lines[position[0] + 1][position[1]] = "-"
            if position[0] > 0 and lines[position[0] - 1][position[1]] == ".":
                next_positions.append([position[0] - 1, position[1]])
                if end:
                    lines[position[0] - 1][position[1]] = "O"
                    total += 1
                else:
                    lines[position[0] - 1][position[1]] = "-"
            if position[1] > 0 and lines[position[0]][position[1] - 1] == ".":
                next_positions.append([position[0], position[1] - 1])
                if end:
                    lines[position[0]][position[1] - 1] = "O"
                    total += 1
                else:
                    lines[position[0]][position[1] - 1] = "-"

        positions = next_positions
        steps += 1

    for line in lines:
        print("".join(line))

    print(total)


if __name__ == "__main__":
    main()

# 302356042520000 + 302885076852801 + 5251277442 + 767526200 + 22312
# 605247138198755
