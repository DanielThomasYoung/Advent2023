def main():
    with open("day15.txt", "r") as file:
        line = file.readline()
        all_lens = line.split(",")

    boxes = {}
    for i in range(256):
        boxes[i] = {}

    for lens in all_lens:
        for index in range(len(lens)):
            if lens[index] == "=":
                box = boxes[find_box(lens[:index])]
                box[lens[:index]] = lens[-1]
                break
            if lens[index] == "-":
                box = boxes[find_box(lens[:index])]
                if lens[:index] in box:
                    del box[lens[:index]]
                break

    total_sum = 0
    for index in range(256):
        box_sum = 0
        for box_position, value in enumerate(list(boxes[index].values())):
            box_sum += (box_position + 1) * int(value)
        total_sum += (index + 1) * box_sum

    print(f"total_sum: {total_sum}")


def find_box(lens):
    temp_sum = 0
    for char in lens:
        temp_sum += ord(char)
        temp_sum *= 17
        temp_sum %= 256
    return temp_sum


if __name__ == "__main__":
    main()
