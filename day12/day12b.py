import asyncio

global cache
cache = {}


def format_line(line):
    split_line = line.split()
    data = list(split_line[0].replace("...", ".").replace("..", "."))
    data = [*data, '?', *data, '?', *data, '?', *data, '?', *data, '.', '.']
    targets = [x for x in split_line[1].split(',')]*5
    return data, targets


def create_cache_key(data, targets):
    cache_key = ''.join([*data, *targets])
    # Reduce all groups of '.' to a single '.'
    return cache_key.replace('.....', ".").replace('...', ".").replace('..', ".")


def recursive_check(line, targets, current_size = 0, current_index = 0, current_target = 0, recursive_sum = 0):
    cache_key = create_cache_key(line, targets)
    if cache_key in cache:
        return cache[cache_key]
    
    cloned_line = line[:]

    for index in range(current_index,len(cloned_line)):
        if current_target == len(targets):
            if '#' in cloned_line[index:]:
                cache[cache_key] = recursive_sum
                return recursive_sum
            cache[cache_key] = 1 + recursive_sum
            return 1 + recursive_sum

        if cloned_line[index] == '#':
            current_size += 1
            if current_size > int(targets[current_target]):
                cache[cache_key] = recursive_sum
                return recursive_sum
            
        elif cloned_line[index] == '?':
            cloned_line[index] = '.'
            recursive_sum += recursive_check(cloned_line, targets, current_size, index, current_target)
            cloned_line[index] = '#'
            current_size += 1
            if current_size > int(targets[current_target]):
                cache[cache_key] = recursive_sum
                return recursive_sum
        else:
            if current_size:
                if current_size == int(targets[current_target]):
                    current_target += 1
                    current_size = 0
                else:
                    cache[cache_key] = recursive_sum
                    return recursive_sum

    cache[cache_key] = recursive_sum
    return recursive_sum


def main():
    total_sum = 0
    with open("day12.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            data, targets = format_line(line)
            total_sum += recursive_check(data, targets)

        print(f"total: {total_sum}")

if __name__ == "__main__":
    main()
