def main():
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    total = 0
    distance = 1

    positions = [(1, 1, "R")]

    while positions:
        next_positions = []
        for position in positions:
            if file_lines[position[0]][position[1]] == "E":
                total = distance
                continue

            next = (position[0] + 1, position[1], "D")
            if (
                file_lines[next[0]][next[1]] != "#"
                and file_lines[next[0]][next[1]] != "^"
                and position[2] != "U"
                and next not in next_positions
            ):
                next_positions.append(next)

            next = (position[0] - 1, position[1], "U")
            if (
                file_lines[next[0]][next[1]] != "#"
                and file_lines[next[0]][next[1]] != "v"
                and position[2] != "D"
                and next not in next_positions
            ):
                next_positions.append(next)

            next = (position[0], position[1] + 1, "R")
            if (
                file_lines[next[0]][next[1]] != "#"
                and file_lines[next[0]][next[1]] != "<"
                and position[2] != "L"
                and next not in next_positions
            ):
                next_positions.append(next)

            next = (position[0], position[1] - 1, "L")
            if (
                file_lines[next[0]][next[1]] != "#"
                and file_lines[next[0]][next[1]] != ">"
                and position[2] != "R"
                and next not in next_positions
            ):
                next_positions.append(next)

        distance += 1
        positions = next_positions

    print("total: ", total)


if __name__ == "__main__":
    main()
