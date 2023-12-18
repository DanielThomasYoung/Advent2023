import asyncio
import concurrent.futures


def format_line(line):
    split_line = line.split()
    data = list(split_line[0])
    data = [*data, '?', *data, '?', *data, '?', *data, '?', *data, '.', '.']
    targets = [int(x) for x in split_line[1].split(',')]*5
    return data, targets

def recursive_check(data, targets, line_index = 0, target_index = 0, current_size = 0, in_recursion = False):
    empty_case = 0

    if in_recursion:
        if current_size:
            if current_size == targets[target_index]:
                target_index += 1
                current_size = 0
            else:
                return empty_case
        line_index += 1

    while line_index < len(data):
        if target_index == len(targets):
            if '#' in data[line_index:]:
                return empty_case
            return 1 + empty_case
        
        if data[line_index] == '#':
            current_size += 1
            if current_size > targets[target_index]:
                return empty_case
        elif data[line_index] == '?':
            empty_case += recursive_check(data, targets,line_index, target_index, current_size, True)
            #lines.append(line[line_index:])
            current_size += 1
            if current_size > targets[target_index]:
                return empty_case
        else:
            if current_size:
                if current_size == targets[target_index]:
                    target_index += 1
                    current_size = 0
                else:
                    return empty_case
        line_index += 1

    return empty_case


def main():
    total_sum = 0

    with open("day12short2.txt", "r") as file:
        lines = file.readlines()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Process each line in parallel
            futures = [executor.submit(process_line, line) for line in lines]

            # Wait for all futures to complete
            concurrent.futures.wait(futures)

            # Retrieve results from completed futures
            for future in futures:
                total_sum += future.result()

    print(f"Total: {total_sum}")

def process_line(line):
    data, targets = format_line(line)
    return recursive_check(data, targets)

if __name__ == "__main__":
    main()
