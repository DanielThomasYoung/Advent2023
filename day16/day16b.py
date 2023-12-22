def main():
    with open('day16.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    best_run = 0

    X_MAX = len(lines[0])
    Y_MAX = len(lines)

    starting_coords = []

    for i in range(X_MAX):
        starting_coords.append((i, -1))
        starting_coords.append((i, Y_MAX))
    
    for i in range(Y_MAX):
        starting_coords.append((-1, i))
        starting_coords.append((X_MAX, i))
    
    print(len(starting_coords))


    for start in starting_coords:
        horizontal_history = set()
        vertical_history = set()

        up_lasers = set()
        down_lasers = set()
        left_lasers = set()
        right_lasers = set()

        if start[0] == -1:
            right_lasers.add(start)
        
        if start[0] == X_MAX:
            left_lasers.add(start)

        if start[1] == -1:
            down_lasers.add(start)
        
        if start[1] == Y_MAX:
            up_lasers.add(start)


        while up_lasers or down_lasers or left_lasers or right_lasers:
            new_up_lasers = set()
            new_down_lasers = set()
            new_left_lasers = set()
            new_right_lasers = set()
            new_horizontal_history = set()
            new_vertical_history = set()

            for laser in up_lasers:
                if laser[1] != 0:
                    new_coords = (laser[0], laser[1] - 1)
                    char = lines[new_coords[1]][new_coords[0]]

                    if char == '\\':
                        new_left_lasers.add(new_coords)

                    elif char == '/':
                        new_right_lasers.add(new_coords)

                    elif char == '-':
                        if new_coords not in horizontal_history:
                            new_left_lasers.add(new_coords)
                            new_right_lasers.add(new_coords)

                    elif new_coords not in vertical_history:
                        new_up_lasers.add(new_coords)

                new_vertical_history.add(laser)

            for laser in down_lasers:
                if laser[1] != Y_MAX - 1:
                    new_coords = (laser[0], laser[1] + 1)
                    char = lines[new_coords[1]][new_coords[0]]

                    if char == '\\':
                        new_right_lasers.add(new_coords)

                    elif char == '/':
                        new_left_lasers.add(new_coords)

                    elif char == '-':
                        if new_coords not in horizontal_history:
                            new_left_lasers.add(new_coords)
                            new_right_lasers.add(new_coords)

                    elif new_coords not in vertical_history:
                        new_down_lasers.add(new_coords)

                new_vertical_history.add(laser)

            for laser in left_lasers:
                if laser[0] != 0:
                    new_coords = (laser[0] - 1, laser[1])
                    char = lines[new_coords[1]][new_coords[0]]

                    if char == '\\':
                        new_up_lasers.add(new_coords)

                    elif char == '/':
                        new_down_lasers.add(new_coords)

                    elif char == '|':
                        if new_coords not in vertical_history:
                            new_up_lasers.add(new_coords)
                            new_down_lasers.add(new_coords)

                    elif new_coords not in horizontal_history:
                        new_left_lasers.add(new_coords)

                new_horizontal_history.add(laser)

            for laser in right_lasers:
                if laser[0] != X_MAX - 1:
                    new_coords = (laser[0] + 1, laser[1])
                    char = lines[new_coords[1]][new_coords[0]]

                    if char == '\\':
                        new_down_lasers.add(new_coords)

                    elif char == '/':
                        new_up_lasers.add(new_coords)

                    elif char == '|':
                        if new_coords not in vertical_history:
                            new_up_lasers.add(new_coords)
                            new_down_lasers.add(new_coords)

                    elif new_coords not in horizontal_history:
                        new_right_lasers.add(new_coords)

                new_horizontal_history.add(laser)


            up_lasers = new_up_lasers
            down_lasers = new_down_lasers
            left_lasers = new_left_lasers
            right_lasers = new_right_lasers
            horizontal_history = horizontal_history.union(new_horizontal_history)
            vertical_history = vertical_history.union(new_vertical_history)
        
        best_run = max(best_run, len(horizontal_history.union(vertical_history)) - 1)
    print(f"total: {best_run}")

    # for index, line in enumerate(lines):
    #     printable = []
    #     for char_index, char in enumerate(lines):
    #         if (char_index, index) in total_history:
    #             printable.append('#')
    #         else:
    #             printable.append('.')
    #     print(printable)

if __name__ == "__main__":
    main()