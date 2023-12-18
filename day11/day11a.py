def expand(lines):
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if '#' not in line:
            new_lines.append(['.'] * len(line))
    return new_lines

def calculate_distance(lines, total_galaxies):
    sum = 0
    galaxy_count = 0

    for line in lines:
        galaxy_count += line.count('#')
        sum += galaxy_count * (total_galaxies - galaxy_count)

    return sum

with open("day11.txt", "r") as file:
    lines = file.readlines()
    total_sum = 0

    galaxy_count = 0
    for line in lines:
        galaxy_count += line.count('#')

    expanded_once = expand(lines)
    total_sum += calculate_distance(expanded_once, galaxy_count)

    transposed_lines = list(map(list, zip(*expanded_once)))
    fully_expanded = expand(transposed_lines)
    total_sum += calculate_distance(fully_expanded, galaxy_count)

    print(f"total_sum: {total_sum}")