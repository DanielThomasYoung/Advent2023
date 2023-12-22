def split_list(original: list) -> list:
    sub = []
    del original[0]
    while original:
        line = original.pop(0)
        if not line:
            return sub
        sub.append(line.split())
    return sub


def adjust(inputs: list[int], mapping: list[int]):
    result = []

    while inputs:
        start_num = inputs.pop(0)
        end_num = start_num + inputs.pop(0)

        for map in mapping:
            start_map = int(map[1])
            end_map = start_map + int(map[2])
            map_adjust = int(map[0]) - start_map

            if end_num < start_map or end_map < start_num:  # no overlap
                continue

            elif start_map <= start_num and end_num <= end_map:  # input ⊆ map
                result.append(start_num + map_adjust)
                result.append(end_num - start_num)
                start_num = end_num
                break

            elif start_num < start_map and end_map < end_num:  # map ⊂ input
                result.append(start_map + map_adjust)
                result.append(end_map - start_map)

                inputs.append(
                    end_map
                )  # send back through loop because we can only process one
                inputs.append(end_num - end_map)

                end_num = start_map

            elif start_num < start_map and end_num <= end_map:  # input left overhang
                result.append(start_map + map_adjust)
                result.append(end_num - start_map)
                end_num = start_map

            else:  # input right overhang
                result.append(start_num + map_adjust)
                result.append(end_map - start_num)
                start_num = end_map

        if start_num != end_num:
            result.append(start_num)
            result.append(end_num - start_num)
    return result


with open("day5.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    seeds = lines.pop(0).split()
    del lines[0]
    del seeds[0]
    current_answer = [int(seed) for seed in seeds]

    while lines:
        maps = split_list(lines)
        current_answer = adjust(current_answer, maps)

    filtered_answer = []
    for index, element in enumerate(current_answer):
        if not index % 2:
            filtered_answer.append(element)
    print(min(filtered_answer))
