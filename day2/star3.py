file_path = "star3.txt"
# 12, 13, 14
total_sum = 0
colors = {"r", "g", "b"}


def convert_to_number(digits):
    sum = 0
    for i in reversed(digits):
        sum = sum * 10 + int(i)
    return sum


with open(file_path, "r") as file:
    for line_number, line in enumerate(file):
        color_max = {"r": 0, "g": 0, "b": 0}
        index = len(line) - 1

        while index != 0:
            if line[index] in colors and line[index - 1] == " ":
                print(line[index])
                current_color = line[index]
                digits = []
                index = index - 2

                while line[index].isdigit():
                    digits.append(line[index])
                    index = index - 1

                sum = convert_to_number(digits)
                color_max[current_color] = max(color_max[current_color], sum)

            index = index - 1

        if color_max["r"] <= 12 and color_max["g"] <= 13 and color_max["b"] <= 14:
            total_sum += line_number + 1
        print(line)
        print(line_number + 1)
        print(color_max)

print(total_sum)
