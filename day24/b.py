from itertools import combinations


def main():
    with open("input.txt", "r") as file:
        file_lines = file.readlines()

    total = 0
    slope_int = []

    low_limit = 200000000000000
    high_limit = 400000000000000

    for line in file_lines:
        [position, velocity] = line.strip().split(" @ ")
        positions = position.split(", ")
        px = int(positions[0])
        py = int(positions[1])
        velocities = velocity.split(", ")
        vx = int(velocities[0])
        vy = int(velocities[1])

        m = vy / vx
        b = py - m * px

        slope_int.append((m, b, px, vx > 0))

    for pair in combinations(slope_int, 2):
        if pair[0][0] != pair[1][0]:
            x = (pair[0][1] - pair[1][1]) / (pair[1][0] - pair[0][0])
            y = pair[0][0] * x + pair[0][1]
            if (
                x >= low_limit
                and x <= high_limit
                and y >= low_limit
                and y <= high_limit
                and (
                    pair[0][3] and pair[0][2] <= x or not pair[0][3] and pair[0][2] >= x
                )
                and (
                    pair[1][3] and pair[1][2] <= x or not pair[1][3] and pair[1][2] >= x
                )
            ):
                total += 1

    print(total)


if __name__ == "__main__":
    main()
