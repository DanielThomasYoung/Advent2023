from math import sqrt, floor, ceil

def roots(total_time, target_time):
    # -x^2 + x*t - y = 0
    print((total_time + sqrt(total_time**2 - 4*target_time)) / 2)
    print((total_time - sqrt(total_time**2 - 4*target_time)) / 2)
    root1 = ceil((total_time + sqrt(total_time**2 - 4*target_time)) / 2)
    root2 = floor((total_time - sqrt(total_time**2 - 4*target_time)) / 2)

    return root1 - root2 - 1

with open("day6.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

    time = lines[0][10:].replace(" ", "")
    distance = lines[1][10:].replace(" ", "")

    print(roots(int(time), int(distance)))
