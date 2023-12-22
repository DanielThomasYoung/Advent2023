total_sum = 0
with open("star5 copy.txt", "r") as file:
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

                add_number = False
                for line_slice in lines[max(line_index - 1, 0) : line_index + 2]:
                    print("")
                    for char_slice in line_slice[
                        max(char_start - 1, 0) : min(
                            char_start + char_length + 1, len(line) - 1
                        )
                    ]:
                        print(char_slice, end="")
                        if char_slice != "." and not char_slice.isdigit():
                            add_number = True

                if add_number:
                    total_sum = total_sum + current_number
                    print(f"    adding: {current_number}")
                else:
                    print("    not adding")

                current_number = 0
print(f"\ntotal sum: {total_sum}")
