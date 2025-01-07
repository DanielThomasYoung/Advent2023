def main():
    total_sum = 0
    with open("day13.txt", "r") as file:
        content = file.read()

    blocks = [block.strip() for block in content.split("\n\n")]
    for block in blocks:
        lines = block.split("\n")
        for line in lines:
            print(line)
        reflection = check_reflections(lines)
        if reflection:
            total_sum += reflection[0]
            print(f"Total: {total_sum}")
        else:
            transposed_lines = list(map(list, zip(*lines)))
            total_sum += check_reflections(transposed_lines)[0] * 100
            print(f"Total: {total_sum}")
    print(total_sum)


def check_reflections(lines):
    reflections = []
    looped = False

    for line in lines:
        if looped and not reflections:
            return []
        looped = True

        if reflections:
            numbers_to_check = reflections
        else:
            numbers_to_check = range(1, len(line))
        new_reflections = []

        for index in numbers_to_check:
            rows_to_reflect = min(index, len(line) - index)

            if (
                line[index - rows_to_reflect : index]
                == line[index : index + rows_to_reflect][::-1]
            ):
                new_reflections.append(index)

        reflections = new_reflections
    return reflections


if __name__ == "__main__":
    main()
