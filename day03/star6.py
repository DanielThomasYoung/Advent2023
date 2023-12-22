total_sum = 0
gears = {}
with open("star5.txt", "r") as file:
    lines = file.readlines()
    for line_index, line in enumerate(lines):
        in_number = False
        current_number = 0
        for char_index, char in enumerate(line):
            if char.isdigit():
                if not in_number:
                    current_number = int(char)
                    char_start = char_index
                    char_length = 1
                    in_number = True
                else:
                    current_number = current_number * 10 + int(char)
                    char_length += 1
            elif in_number:
                in_number = False

                for inner_line_index, line_slice in enumerate(
                    lines[max(line_index - 1, 0) : line_index + 2]
                ):
                    for inner_char_index, char_slice in enumerate(
                        line_slice[
                            max(char_start - 1, 0) : char_start + char_length + 1
                        ]
                    ):
                        if char_slice == "*":
                            line_edge_case = not line_index
                            char_edge_case = not char_start

                            gear_index = (
                                str(line_index + inner_line_index - 1 + line_edge_case)
                                + "*"
                                + str(
                                    char_start + inner_char_index - 1 + char_edge_case
                                )
                            )
                            if gear_index in gears:
                                total_sum += current_number * gears[gear_index]
                            else:
                                gears[gear_index] = current_number
                                print(f"gears: {gears}")

                current_number = 0

print(f"total_sum: {total_sum}")
