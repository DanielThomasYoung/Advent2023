def main():
    with open("day18.txt", "r") as file:
        lines = [line.strip().split() for line in file.readlines()]

    max_up = 0
    max_down = 0
    max_left = 0
    max_right = 0

    walls = {(0, 0)}
    shovel = (0, 0)

    for line in lines:
        if line[0] == "U":
            for _ in range(int(line[1])):
                shovel = (shovel[0], shovel[1] - 1)
                walls.add(shovel)
            max_up = min(max_up, shovel[1])

        if line[0] == "D":
            for _ in range(int(line[1])):
                shovel = (shovel[0], shovel[1] + 1)
                walls.add(shovel)
            max_down = max(max_down, shovel[1])

        if line[0] == "L":
            for _ in range(int(line[1])):
                shovel = (shovel[0] - 1, shovel[1])
                walls.add(shovel)
            max_left = min(max_left, shovel[0])

        if line[0] == "R":
            for _ in range(int(line[1])):
                shovel = (shovel[0] + 1, shovel[1])
                walls.add(shovel)
            max_right = max(max_right, shovel[0])

    edges = set()
    edge_history = set()


    for i in range(max_up - 1, max_down + 2):
        edges.add((max_left - 1, i))
        edges.add((max_right + 1, i))

    for i in range(max_left - 1, max_right + 2):
        edges.add((i, max_up - 1))
        edges.add((i, max_down + 1))

    offset = len(edges)

    while edges:
        new_edges = set()
        for edge in edges:
            new_coord = (edge[0], edge[1] - 1)  # up
            if new_coord[1] >= max_up and new_coord not in edge_history and new_coord not in walls:
                new_edges.add(new_coord)

            new_coord = (edge[0], edge[1] + 1)  # down
            if new_coord[1] <= max_down and new_coord not in edge_history and new_coord not in walls:
                new_edges.add(new_coord)

            new_coord = (edge[0] - 1, edge[1])  # left
            if new_coord[0] >= max_left and new_coord not in edge_history and new_coord not in walls:
                new_edges.add(new_coord)

            new_coord = (edge[0] + 1, edge[1])  # right
            if new_coord[0] <= max_right and new_coord not in edge_history and new_coord not in walls:
                new_edges.add(new_coord)

        edge_history = edge_history.union(edges)
        edges = new_edges


    # for index in range(max_up, max_down + 1):
    #     printable = []
    #     for char_index in range(max_left, max_right + 1):
    #         if (char_index, index) in walls:
    #             printable.append('#')
    #         elif (char_index, index) in edge_history:
    #             printable.append('X')
    #         else:
    #             printable.append('.')
    #     print(printable)

    square = (max_right - max_left + 1) * (max_down - max_up + 1)
    outside = len(edge_history) - offset
    print(f"total: {square - outside}")


if __name__ == "__main__":
    main()