with open("day10.txt", "r") as file:
    lines = file.readlines()

    y = 64
    x = 62
    d = 'D'

    crossing_up = [[0] * len(lines[0]) for _ in range(len(lines))]
    crossing_down = [[0] * len(lines[0]) for _ in range(len(lines))]
    main_pipe = [[0] * len(lines[0]) for _ in range(len(lines))]
    main_pipe[63][62] = 1
    crossing_down[64][62] = 2

    while lines[y][x] != 'S':
        main_pipe[y][x] = 1

        if d == 'R':
            x += 1
            next_char = lines[y][x]

            if next_char == 'J':
                d = 'U'
                crossing_up[y][x] = 1

            elif next_char == '-':
                d = 'R'

            else:
                d = 'D'
                crossing_down[y][x] = 1

        elif d == 'L':
            x -= 1
            next_char = lines[y][x]

            if next_char == 'L':
                d = 'U'
                crossing_up[y][x] = 1

            elif next_char == '-':
                d = 'L'

            else:
                d = 'D'
                crossing_down[y][x] = 1

        elif d == 'U':
            y -= 1
            next_char = lines[y][x]

            if next_char == '|':
                crossing_up[y][x] = 2
                d = 'U'

            elif next_char == 'F':
                crossing_up[y][x] = 1
                d = 'R'

            else:
                crossing_up[y][x] = 1
                d = 'L'            

        elif d == 'D':
            y += 1
            next_char = lines[y][x]

            if next_char == 'L':
                crossing_down[y][x] = 1
                d = 'R'

            elif next_char == 'J':
                crossing_down[y][x] = 1
                d = 'L'

            else:
                crossing_down[y][x] = 2
                d = 'D'            

    main_pipe[y][x] = 1

    total_sum = 0
    for index_y in range(len(lines)):
        crossing_sum = 0
        for index_x in range(len(lines[0])):
            crossing_sum += crossing_up[index_y][index_x] - crossing_down[index_y][index_x]

            if not main_pipe[index_y][index_x] and crossing_sum != 0:
                total_sum += 1

    print(f"total_sum: {total_sum}")
