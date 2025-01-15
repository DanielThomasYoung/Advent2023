def main():
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    positions = [[[0 for _ in range(300)] for _ in range(10)] for _ in range(10)]

    pre_sorted_lines = []
    stacked = {}

    for line in file_lines:
        ends = line.strip().split("~")
        first_coords = ends[0].split(",")
        second_coords = ends[1].split(",")

        first_coords = [int(coord) for coord in first_coords]
        second_coords = [int(coord) for coord in second_coords]

        pre_sorted_lines.append((first_coords, second_coords))

    sorted_lines = sorted(pre_sorted_lines, key=lambda x: (x[0][2]))

    total = 0

    line_number = 0

    for line in sorted_lines:
        (first_coords, second_coords) = line
        line_number += 1

        x_diff = second_coords[0] - first_coords[0]
        y_diff = second_coords[1] - first_coords[1]
        z_diff = second_coords[2] - first_coords[2]

        keep_looping = True

        under = set()

        if x_diff:
            y = first_coords[1]
            z = first_coords[2]
            while keep_looping:
                for x in range(first_coords[0], second_coords[0] + 1):
                    if z == 1:
                        for final_x in range(first_coords[0], second_coords[0] + 1):
                            positions[final_x][y][z] = line_number
                        keep_looping = False
                    if positions[x][y][z - 1]:
                        under.add(positions[x][y][z - 1])
                        for final_x in range(first_coords[0], second_coords[0] + 1):
                            positions[final_x][y][z] = line_number
                        keep_looping = False
                z -= 1

        elif y_diff:
            x = first_coords[0]
            z = first_coords[2]
            while keep_looping:
                for y in range(first_coords[1], second_coords[1] + 1):
                    if z == 1:
                        for final_y in range(first_coords[1], second_coords[1] + 1):
                            positions[x][final_y][z] = line_number
                        keep_looping = False
                    if positions[x][y][z - 1]:
                        under.add(positions[x][y][z - 1])
                        for final_y in range(first_coords[1], second_coords[1] + 1):
                            positions[x][final_y][z] = line_number
                        keep_looping = False
                z -= 1

        else:
            x = first_coords[0]
            y = first_coords[1]
            z = first_coords[2]
            while keep_looping:
                if z == 1:
                    for final_z in range(z, z + z_diff + 1):
                        positions[x][y][final_z] = line_number
                    keep_looping = False
                if positions[x][y][z - 1]:
                    under.add(positions[x][y][z - 1])
                    for final_z in range(z, z + z_diff + 1):
                        positions[x][y][final_z] = line_number
                    keep_looping = False
                z -= 1

        if len(under) > 0:
            for _, stack in stacked.items():
                if under <= stack:
                    stack.add(line_number)

        if len(under) == 1:
            single = under.pop()
            if single not in stacked:
                stacked[single] = set()
            stacked[single].add(line_number)

    total = 0

    for _, stack in stacked.items():
        total += len(stack)

    print(total)


if __name__ == "__main__":
    main()
