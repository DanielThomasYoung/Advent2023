global workflows
global convert_letter
workflows = {}
convert_letter = {'x': 0, 'm': 1, 'a': 2, 's': 3}


def main():
    with open("day19b.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

    parts = [1, 4000, 1, 4000, 1, 4000, 1, 4000]
    

    while lines:
        line = lines.pop()
        split = line[:-1].split('{')
        key = split[0]

        rules = split[1].split(',')

        for index in range(len(rules)):
            rules[index] = rules[index].split(':')

        workflows[key] = rules
    # End of formatting
        
    return recursive(parts)

def recursive(parts, workflow = 'in', recursive_sum = 0):
    #print(f"workflow: {workflow}")


    while True:
        #print(f"workflow: {workflow}")

        if workflow == 'A':
            #print(f"x: {parts[1]} - {parts[0]} m: {parts[3]} - {parts[2]} a: {parts[5]} - {parts[4]} s: {parts[7]} - {parts[6]}")
            return recursive_sum + (parts[1]-parts[0]+1) * (parts[3]-parts[2]+1) * (parts[5]-parts[4]+1) * (parts[7]-parts[6]+1)
        if workflow == 'R':
            return recursive_sum

        rules = workflows[workflow]
        for rule in rules:
            new_parts = parts[:]

            if len(rule) == 1:
                return recursive_sum + recursive(parts, rule[0])

            operator = rule[0][1]
            part_index = convert_letter[rule[0][0]]
            compare_number = int(rule[0][2:])

            if operator == '>':
                if parts[part_index*2] > compare_number:
                    return recursive_sum + recursive(parts, rule[1])

                elif parts[part_index*2+1] > compare_number:
                    #print(f"parts: {parts}")
                    new_parts[part_index*2] = compare_number + 1
                    parts[part_index*2+1] = compare_number
                    #print(f"parts: {parts}")

                    recursive_sum += recursive(new_parts, rule[1])

            else:
                if parts[part_index*2+1] < compare_number:
                    return recursive_sum + recursive(parts, rule[1])

                elif parts[part_index*2] < compare_number:
                    new_parts[part_index*2+1] = compare_number - 1
                    parts[part_index*2] = compare_number
                    recursive_sum += recursive(new_parts, rule[1])




if __name__ == "__main__":
    print(main())