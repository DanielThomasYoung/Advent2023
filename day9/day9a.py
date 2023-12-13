with open("day9.txt", "r") as file:
    lines = file.readlines()
    total_sum = 0
    for line in lines:
        formatted_line = line.split()
        for index, value in enumerate(formatted_line):
            pascal = comb(len(formatted_line), index)                
            total_sum += int(value)*pascal*(-1)**(len(formatted_line)-index+1)
    print(f"total: {total_sum}")