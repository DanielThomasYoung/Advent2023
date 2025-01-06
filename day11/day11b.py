def calculate_distance(lines, total_galaxies):
    sum = 0
    galaxy_count = 0

    for line in lines:
        galaxy_count += line.count('#')
        if line.count('#') == 0:
            multiplier = 1000000
        else:
            multiplier = 1
        sum += galaxy_count * (total_galaxies - galaxy_count) * multiplier

    return sum

with open("input.txt", "r") as file:
    lines = file.readlines()
    total_sum = 0

    galaxy_count = 0
    for line in lines:
        galaxy_count += line.count('#')

    total_sum += calculate_distance(lines, galaxy_count)

    transposed_lines = list(map(list, zip(*lines)))
    total_sum += calculate_distance(transposed_lines, galaxy_count)

    print(f"total_sum: {total_sum}")