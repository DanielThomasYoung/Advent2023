def main():
    with open("day15.txt", "r") as file:
        line = file.readline()
    
    total = 0
    temp_sum = 0
    for char in line:
        if char == ',':
            print(f"adding: {temp_sum}")
            total += temp_sum
            temp_sum = 0
        else:
            temp_sum += ord(char)
            print(f"temp_sum: {temp_sum}")
            temp_sum *= 17
            print(f"temp_sum: {temp_sum}")
            temp_sum %= 256
    
    total += temp_sum
    print(total)

if __name__ == "__main__":
    main()