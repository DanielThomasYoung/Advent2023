def main():
    with open('sample.txt', 'r') as file:
        file_lines = file.readlines()

    lines = []
    for line in file_lines:
        lines.append(list(line.strip()))

    positions = set()  # x, y, plot_x, plot_y
    steps = 0
    total = set()

    for line_index in range(len(lines)):
        for char_index in range(len(lines[0])):
            if lines[line_index][char_index] == 'S':
                positions.add((line_index, char_index, 0, 0))
                lines[line_index][char_index] = '.'

    while steps < 5000:
        print(steps)
        #26501365

        end = steps % 2
        next_positions = set()

        for position in positions:
            next_postion = (position[0] + 1, position[1], position[2], position[3])
            next_postion = check_location(next_postion, next_positions, lines, end, total)

            next_postion = (position[0] - 1, position[1], position[2], position[3])
            next_postion = check_location(next_postion, next_positions, lines, end, total)

            next_postion = (position[0], position[1] + 1, position[2], position[3])
            next_postion = check_location(next_postion, next_positions, lines, end, total)


            next_postion = (position[0], position[1] - 1, position[2], position[3])
            next_postion = check_location(next_postion, next_positions, lines, end, total)




        positions = next_positions
        steps += 1

        # for line in lines:
            # print(''.join(line))        

    print(len(total))



def check_location(position: tuple, next_positions: set, lines: list, end: int, total: set) -> bool:
    x = position[0]
    y = position[1]
    plot_x = position[2]
    plot_y = position[3]

    if x < 0:
        plot_x -= 1
        x = len(lines) - 1
    elif x >= len(lines):
        plot_x += 1
        x = 0
    if y < 0:
        plot_y -= 1
        y = len(lines[0]) - 1
    elif y >= len(lines[0]):
        plot_y += 1
        y = 0

    if lines[x][y] == '.':
        if (x, y, plot_x, plot_y) not in total:
            next_positions.add((x, y, plot_x, plot_y))
        if end:
            total.add((x, y, plot_x, plot_y))







if __name__ == '__main__':
    main()