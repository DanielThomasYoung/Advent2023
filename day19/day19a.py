def main():
    with open("day19.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

    workflows = {}
    parts = []

    line = lines.pop()
    while line != "":
        formatted = line[1:-1].split(',')
        for index in range(4):
            formatted[index] = formatted[index][2:]

        parts.append(formatted)
        line = lines.pop()
    
    while lines:
        line = lines.pop()
        split = line[:-1].split('{')
        key = split[0]

        rules = split[1].split(',')

        for index in range(len(rules)):
            rules[index] = rules[index].split(':')

        workflows[key] = rules
    # End of formatting

    total = 0
    for part in parts:
        x = int(part[0])
        m = int(part[1])
        a = int(part[2])
        s = int(part[3])

        workflow = 'in'
        while True:

            if workflow == 'A':
                total += x+m+a+s
                break
            if workflow == 'R':
                break

            rules = workflows[workflow]
            for rule in rules:
                if len(rule) == 1:
                    workflow = rule[0]
                    break
                    
                # example:x < 3754
                if eval(f"{rule[0][0]} {rule[0][1]} {rule[0][2:]}"):
                    workflow = rule[1]
                    break

    print(total)
   





if __name__ == "__main__":
    main()