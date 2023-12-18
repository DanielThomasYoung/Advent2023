def main():
    total_sum = 0
    with open('day13.txt', 'r') as file:
        content = file.read()

    blocks = [block.strip() for block in content.split('\n\n')]
    for block in blocks:
        lines = block.split('\n')
        for line in lines:
            print(line)
        off_by_one = check_reflections(lines)
        min_key = min(off_by_one, key=lambda k: off_by_one[k])

        if off_by_one[min_key] == 1:
            print(f"off_by_one: {off_by_one}")
            print(f"min_key: {min_key}")
            total_sum += min_key

        else:
            transposed_lines = list(map(list, zip(*lines)))
            off_by_one = check_reflections(transposed_lines)
            min_key = min(off_by_one, key=lambda k: off_by_one[k])
            total_sum += min_key*100
            print(f"off_by_one: {off_by_one}")
            print(f"min_key: {min_key}")
    print(total_sum)


def check_reflections(lines):
    off_by_one = {}

    for line in lines:
        for index in range(1, len(line)):
            rows_to_reflect = min(index, len(line) - index)
            left = line[index-rows_to_reflect:index]
            right = line[index:index+rows_to_reflect][::-1]

            count = 0
            for left_char, right_char in zip(left, right):
                if left_char != right_char:
                    count += 1
            if count == 1:
                if index in off_by_one:
                    off_by_one[index] += 1
                else:
                    off_by_one[index] = 1
            elif count > 1:
                off_by_one[index] = 999
                        
    return off_by_one

if __name__ == "__main__":
    main()