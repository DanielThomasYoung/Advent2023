from dataclasses import dataclass


def main():
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    total = 0
    nodes = {}
    new_nodes = {"1 1": Node(1, 1, ["D"], {})}

    def node_search(key, x, y, direction):
        distance = 0

        while True:
            distance += 1
            next = []
            if file_lines[x + 1][y] != "#" and direction != "U":
                next.append((x + 1, y, "D"))

            if file_lines[x - 1][y] != "#" and direction != "D":
                next.append((x - 1, y, "U"))

            if file_lines[x][y + 1] != "#" and direction != "L":
                next.append((x, y + 1, "R"))

            if file_lines[x][y - 1] != "#" and direction != "R":
                next.append((x, y - 1, "L"))

            if len(next) > 1 or file_lines[x][y] == "E":
                directions = []

                new_key = f"{x} {y}"

                if new_key not in nodes:
                    for n in next:
                        directions.append(n[2])
                    new_nodes[new_key] = Node(x, y, directions, {key: distance})
                nodes[key].connections[f"{x} {y}"] = distance

                return

            if len(next) == 1:
                x = next[0][0]
                y = next[0][1]
                direction = next[0][2]

            if len(next) == 0:
                return

    def recursive_walk(key, distance, history):
        nonlocal total
        for key, value in nodes[key].connections.items():
            if key not in history:
                new_history = history.copy()
                new_history.append(key)
                total = max(total, distance + value)
                recursive_walk(key, distance + value, new_history)

    while new_nodes:
        key, current_node = new_nodes.popitem()
        nodes[key] = current_node

        for direction in current_node.directions:
            if direction == "R":
                node_search(key, current_node.x, current_node.y + 1, "R")
            if direction == "L":
                node_search(key, current_node.x, current_node.y - 1, "L")
            if direction == "U":
                node_search(key, current_node.x - 1, current_node.y, "U")
            if direction == "D":
                node_search(key, current_node.x + 1, current_node.y, "D")

    recursive_walk("1 1", 0, ["1 1"])
    print(total)


@dataclass
class Node:
    x: int
    y: int
    directions: list
    connections: dict


if __name__ == "__main__":
    main()
