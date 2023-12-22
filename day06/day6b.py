from math import sqrt, floor, ceil


with open("day6.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

    time = lines[0][10:].replace(" ", "")
    distance = lines[1][10:].replace(" ", "")

    root1 = ceil((int(time) + sqrt(int(time)**2 - 4 * int(distance))) / 2)
    root2 = floor((int(time) - sqrt(int(time)**2 - 4 * int(distance))) / 2)

    print(root1 - root2 - 1)
