total_sum = 0
with open("day14.txt", "r") as file:
    lines = file.readlines()
transposed_lines = list(map("".join, zip(*lines)))

for line in transposed_lines:
    latest_square = -1
    for index in range(len(line)):
        char = line[index]
        if char == "O":
            latest_square += 1
            total_sum += len(line) - latest_square
        elif char == "#":
            latest_square = index

print(f"total sum: {total_sum}")
