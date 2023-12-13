import math
with open("day4.txt", "r") as file:
    total = 0
    lines = file.readlines()
    for line in lines:
        current_add = 0.5
        two_parts = line.split('|')
        left = two_parts[0].split()
        right = two_parts[1].split()
        for number in left:
            if number in right:
                current_add *= 2
        total += math.floor(current_add)
    print(total)

