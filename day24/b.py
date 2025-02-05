import sympy as sp


def main():
    with open("sample.txt", "r") as file:
        file_lines = file.readlines()

    vectors = []

    for line in file_lines:
        [position, velocity] = line.strip().split(" @ ")
        positions = position.split(", ")
        px = int(positions[0])
        py = int(positions[1])
        pz = int(positions[2])
        velocities = velocity.split(", ")
        vx = int(velocities[0])
        vy = int(velocities[1])
        vz = int(velocities[2])

        vectors.append([1, -vy, -px, -1, vx, py, py * vx - px * vy])

    matrix = sp.Matrix(vectors)
    rref_matrix, _ = matrix.rref()

    print(rref_matrix)

    # px1*vy1 - px1*vy2 - px2*vy1 + px2*vy2 = py1*vx1 - py1*vx2 - py2*vx1 + py2*vx2

    # px1*vy1 - px1*vy2 - px2*vy1 - py1*vx1 + py1*vx2 + py2*vx1 = py2*vx2 - px2*vy2
    #              px        vy                  py        vx

    # 1, -vy2, -px2, -1, vx2, py2 = py2*vx2 - px2*vy2


if __name__ == "__main__":
    main()
