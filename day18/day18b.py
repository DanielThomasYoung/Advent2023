def main():
    with open("day18.txt", "r") as file:
        lines = [line.strip().split() for line in file.readlines()]


    vertical_lines = []  # [x, low y, high y]
    horizontal_lines = []  # [low x, high x, y]
    shovel = (0, 0)


    for line in lines:
        length = int(line[2][2:7], 16)
        direction = line[2][7]
        if direction == "3":
            vertical_lines.append((shovel[0], shovel[1] - length, shovel[1]))
            shovel = (shovel[0], shovel[1] - length)

        elif direction == "1":
            vertical_lines.append((shovel[0], shovel[1], shovel[1] + length))
            shovel = (shovel[0], shovel[1] + length)

        elif direction == "2":
            horizontal_lines.append((shovel[0] - length, shovel[0], shovel[1]))
            shovel = (shovel[0] - length, shovel[1])

        else:
            horizontal_lines.append((shovel[0], shovel[0] + length, shovel[1]))
            shovel = (shovel[0] + length, shovel[1])
    # Done digging, time to count
            
    horizontal_lines = sorted(horizontal_lines, key=lambda x: x[2])

    total = 0
    while vertical_lines:
        vertical_lines = sorted(vertical_lines, key=lambda x: (x[1], x[0]))

        lowest = vertical_lines[0][1]
        current_block = []
        while vertical_lines and vertical_lines[0][1] == lowest:
            current_block.append(vertical_lines.pop(0))

        if vertical_lines:  # Determine how far to process. This was before I stored the horizontal lines
            stopping_point = vertical_lines[0][1]
            for c in current_block:
                stopping_point = min(stopping_point, c[2])
        else:  # final block
            stopping_point = current_block[0][2]
            current_block = sorted(current_block, key=lambda x: (x[1], x[2]))

        # Lines passing stopping point are split and processed in the next block
        for current_corner in current_block:  
            if current_corner[2] - stopping_point > 0:
                vertical_lines.append((current_corner[0], stopping_point, current_corner[2]))

        # Used later to calculated area of block
        vertical = stopping_point - current_block[0][1]

        # A bunch of edge cases.
        # Without this, the answer gets close by counting the area of squares, 
        # but misses the horizontal lines
        for horizonal in horizontal_lines:
            if horizonal[2] == current_block[0][1]:
                added = False
                for index in range(len(current_block)):
                    if current_block[index][0] == horizonal[0]:
                        added = True
                        if index % 2:
                            # Add missing horizontal edge
                            total += horizonal[1] - horizonal[0] - 1

                            edge_case = 1
                            for i in current_block:
                                if i[0] == horizonal[1]:
                                    edge_case = 0
                                    break
                            # Edge extending outside blocks
                            total += edge_case
                        break
                    
                    # Same as above, but we need to consider left and right side
                    elif current_block[index][0] == horizonal[1]:
                        added = True
                        # The mod 2 determines if the horizontal line is inside a block (already counted)
                        # or outside (needs to be added)
                        if not index % 2:
                            total += horizonal[1] - horizonal[0] - 1

                            edge_case = 1
                            for i in current_block:
                                if i[0] == horizonal[0]:
                                    edge_case = 0
                                    break
                            total += edge_case
                        break
                
                # Some horizontal lines were not touching any blocks. These look like the tops of towers
                if not added:
                    print(f"current_block: {current_block}")
                    count = 0
                    for c in current_block:
                        if c[0] < horizonal[0]:
                            count += 1
                        
                    # The mod 2 determines if the horizontal line is inside a block (already counted)
                    # or outside a block (needs to be added)
                    if not count % 2:
                        total += horizonal[1] - horizonal[0] + 1

        while current_block:
            odd = current_block.pop()
            even = current_block.pop()
            print(f"normal square add: {(odd[0] - even[0] + 1)*vertical}")
            print(f"h: {odd[0] - even[0] + 1}, v: {vertical}")
            total += (odd[0] - even[0] + 1) * vertical
        print("")
    
    # Add final top line
    top = horizontal_lines[-1][2]
    for horizonal in horizontal_lines:
        if horizonal[2] == top:
            print(f"add final top {horizonal[1] - horizonal[0] + 1}")
            total += horizonal[1] - horizonal[0] + 1

    print(total)


if __name__ == "__main__":
    main()