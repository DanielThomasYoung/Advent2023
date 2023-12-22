with open("day4.txt", "r") as file:
    lines = file.readlines()
    copies = [1] * len(lines)

    for line_index, line in enumerate(lines):
        count = 0
        two_parts = line.split("|")
        left = two_parts[0].split()
        right = two_parts[1].split()

        for number in left:
            if number in right:
                count += 1

        for i in range(1, count + 1):
            copies[line_index + i] += copies[line_index]

    print(sum(copies))
