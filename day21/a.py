def main():
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    lines = [["#"] * (len(file_lines[0]) + 1)]
    for line in file_lines:
        lines.append(["#"] + list(line.strip()) + ["#"])
    lines.append(["#"] * (len(file_lines[0]) + 1))

    positions = []
    steps = 0
    total = 0

    for line_index in range(len(lines)):
        for char_index in range(len(lines[0])):
            if lines[line_index][char_index] == "S":
                positions.append([line_index, char_index])
                lines[line_index][char_index] = "."

    while steps < 64:
        end = steps % 2
        next_positions = []
        for position in positions:
            if lines[position[0]][position[1] + 1] == ".":
                next_positions.append([position[0], position[1] + 1])
                if end:
                    lines[position[0]][position[1] + 1] = "O"
                    total += 1
                else:
                    lines[position[0]][position[1] + 1] = "-"
            if lines[position[0] + 1][position[1]] == ".":
                next_positions.append([position[0] + 1, position[1]])
                if end:
                    lines[position[0] + 1][position[1]] = "O"
                    total += 1
                else:
                    lines[position[0] + 1][position[1]] = "-"
            if lines[position[0] - 1][position[1]] == ".":
                next_positions.append([position[0] - 1, position[1]])
                if end:
                    lines[position[0] - 1][position[1]] = "O"
                    total += 1
                else:
                    lines[position[0] - 1][position[1]] = "-"
            if lines[position[0]][position[1] - 1] == ".":
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
