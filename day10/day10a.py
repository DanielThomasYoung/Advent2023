with open("day10.txt", "r") as file:
    lines = file.readlines()
    count = 1
    y = 64
    x = 62
    d = 'D'

    while lines[y][x] != 'S':
        if d == 'R':
            x += 1
            next_char = lines[y][x]
            if next_char == 'J':
                d = 'U'
            elif next_char == '-':
                d = 'R'
            else:
                d = 'D'

        elif d == 'L':
            x -= 1
            next_char = lines[y][x]
            if next_char == 'L':
                d = 'U'
            elif next_char == '-':
                d = 'L'
            else:
                d = 'D'

        elif d == 'U':
            y -= 1
            next_char = lines[y][x]
            if next_char == '|':
                d = 'U'
            elif next_char == 'F':
                d = 'R'
            else:
                d = 'L'            

        elif d == 'D':
            y += 1
            next_char = lines[y][x]
            if next_char == 'L':
                d = 'R'
            elif next_char == '|':
                d = 'D'
            else:
                d = 'L'            

        count += 1
        print(f"x: {x}, y: {y}, d: {d}")
        print(f"count: {count/2}")

