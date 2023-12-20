def main():
    with open("d17.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

    locations = {}

    locations[(0, 0)] = [
        int(lines[0][0]),
        "r",
        0,
        True,
    ]  # heat, current direction, straight line, active

    for _ in range(10):
        new_locations = {}
        for coords in locations:
            if locations[coords][3]:
                for direction in calculate_directions(
                    locations[coords][1], locations[coords][2]
                ):
                    if direction == "u" and coords[1] != 0:
                        new_coords = (coords[0], coords[1] - 1)
                        if new_coords in locations and locations[new_coords][
                            0
                        ] < locations[coords][0] + int(
                            lines[new_coords[1]][new_coords[0]]
                        ):
                            pass
                        elif new_coords in new_locations and new_locations[new_coords][
                            0
                        ] < locations[coords][0] + int(
                            lines[new_coords[1]][new_coords[0]]
                        ):
                            pass
                        else:
                            new_locations[new_coords] = [
                                locations[coords][0]
                                + int(lines[new_coords[1]][new_coords[0]]),
                                direction,
                                locations[coords][2]
                                + (direction == locations[coords][1]),
                                True,
                            ]

                    if direction == "d" and coords[1] != len(lines):
                        new_coords = (coords[0], coords[1] + 1)
                        if new_coords in locations and locations[new_coords][
                            0
                        ] < locations[coords][0] + int(
                            lines[new_coords[1]][new_coords[0]]
                        ):
                            pass
                        elif new_coords in new_locations and new_locations[new_coords][
                            0
                        ] < locations[coords][0] + int(
                            lines[new_coords[1]][new_coords[0]]
                        ):
                            pass
                        else:
                            new_locations[new_coords] = [
                                locations[coords][0]
                                + int(lines[new_coords[1]][new_coords[0]]),
                                direction,
                                locations[coords][2]
                                + (direction == locations[coords][1]),
                                True,
                            ]

                    if direction == "l" and coords[0] != 0:
                        new_coords = (coords[0] - 1, coords[1])
                        if new_coords in locations and locations[new_coords][
                            0
                        ] < locations[coords][0] + int(
                            lines[new_coords[1]][new_coords[0]]
                        ):
                            pass
                        elif new_coords in new_locations and new_locations[new_coords][
                            0
                        ] < locations[coords][0] + int(
                            lines[new_coords[1]][new_coords[0]]
                        ):
                            pass
                        else:
                            new_locations[new_coords] = [
                                locations[coords][0]
                                + int(lines[new_coords[1]][new_coords[0]]),
                                direction,
                                locations[coords][2]
                                + (direction == locations[coords][1]),
                                True,
                            ]

                    if direction == "r" and coords[0] != len(lines[0]):
                        new_coords = (coords[0] + 1, coords[1])
                        if new_coords in locations and locations[new_coords][
                            0
                        ] < locations[coords][0] + int(
                            lines[new_coords[1]][new_coords[0]]
                        ):
                            pass
                        elif new_coords in new_locations and new_locations[new_coords][
                            0
                        ] < locations[coords][0] + int(
                            lines[new_coords[1]][new_coords[0]]
                        ):
                            pass
                        else:
                            new_locations[new_coords] = [
                                locations[coords][0]
                                + int(lines[new_coords[1]][new_coords[0]]),
                                direction,
                                locations[coords][2]
                                + (direction == locations[coords][1]),
                                True,
                            ]

            locations[coords][3] = False
        if (len(lines[0]), len(lines)) in new_locations:
            print(new_locations[(len(lines[0]), len(lines))])
            break
        locations.update(new_locations)
    print(locations)


def calculate_directions(direction, straight):
    if straight == 3:
        if direction == "u" or direction == "d":
            return ["l", "r"]
        return ["u", "d"]

    if direction == "u":
        return ["u", "l", "r"]
    if direction == "d":
        return ["d", "l", "r"]
    if direction == "l":
        return ["u", "d", "l"]
    return ["u", "d", "r"]


if __name__ == "__main__":
    main()
