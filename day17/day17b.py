def main():
    with open("day17.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

    MAX_X = len(lines[0]) - 1
    MAX_Y = len(lines) - 1

    locations = {}
    locations[(0, 0)] = [[
        0,
        "r",
        0,
        True,
    ]]  # heat, current direction, straight line, active

    for _ in range(500):
        new_locations = {}
        for coords in locations:
            for stored_value in locations[coords]:
                if stored_value[3]:
                    for direction in calculate_directions(stored_value[1], stored_value[2]):
                        if direction == "u" and coords[1] > 0:
                            new_coords = (coords[0], coords[1] - 1)

                            if direction == stored_value[1]:
                                new_straight = stored_value[2] + 1
                            else:
                                new_straight = 1

                            if new_coords not in new_locations:
                                new_locations[new_coords] = []

                            new_locations[new_coords].append([
                                stored_value[0]
                                + int(lines[new_coords[1]][new_coords[0]]),
                                direction,
                                new_straight,
                                True,
                            ])

                        if direction == "d" and coords[1] < MAX_Y:
                            new_coords = (coords[0], coords[1] + 1)

                            if direction == stored_value[1]:
                                new_straight = stored_value[2] + 1
                            else:
                                new_straight = 1

                            if new_coords not in new_locations:
                                new_locations[new_coords] = []

                            new_locations[new_coords].append([
                                stored_value[0]
                                + int(lines[new_coords[1]][new_coords[0]]),
                                direction,
                                new_straight,
                                True,
                            ])

                        if direction == "l" and coords[0] > 0:
                            new_coords = (coords[0] - 1, coords[1])
     
                            if direction == stored_value[1]:
                                new_straight = stored_value[2] + 1
                            else:
                                new_straight = 1

                            if new_coords not in new_locations:
                                new_locations[new_coords] = []

                            new_locations[new_coords].append([
                                stored_value[0]
                                + int(lines[new_coords[1]][new_coords[0]]),
                                direction,
                                new_straight,
                                True,
                            ])

                        if direction == "r" and coords[0] < MAX_X:
                            new_coords = (coords[0] + 1, coords[1])

                            if direction == stored_value[1]:
                                new_straight = stored_value[2] + 1
                            else:
                                new_straight = 1

                            if new_coords not in new_locations:
                                new_locations[new_coords] = []

                            new_locations[new_coords].append([
                                stored_value[0]
                                + int(lines[new_coords[1]][new_coords[0]]),
                                direction,
                                new_straight,
                                True,
                            ])

                stored_value[3] = False
                if not coords in new_locations:
                    new_locations[coords] = []
                new_locations[coords].append(stored_value)
        
        locations = new_locations

        # Cleanup
        for coords in locations:
            last = len(locations[coords]) - 1
            while last > 0:
                compared_index = last - 1
                while compared_index > 0:
                    if locations[coords][compared_index][1:3] == locations[coords][last][1:3]:
                        if locations[coords][compared_index][0] >= locations[coords][last][0]:
                            locations[coords][compared_index][0] = locations[coords][last][0]
                            locations[coords][compared_index][3] = locations[coords][last][3]
                        del(locations[coords][last])
                        break
                    compared_index -= 1
                last -= 1

    # Check for completion
    if (MAX_X, MAX_Y) in locations:
        answer = 9999
        for data in locations[(MAX_X, MAX_Y)]:
            answer = min(answer, data[0])

    print(f"answer: {answer}")




def calculate_directions(direction, straight):
    if straight < 4:
        return [direction]

    if straight == 10:
        if direction == "u" or direction == "d":
            return ["l", "r"]
        return ["u", "d"]

    if direction == "u":
        return ["u", "l", "r"]
    if direction == "d":
        return ["d", "l", "r"]
    if direction == "l":
        return ["l", "u", "d"]
    return ["u", "d", "r"]


if __name__ == "__main__":
    main()
