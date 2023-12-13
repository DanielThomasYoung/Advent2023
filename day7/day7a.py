def find_hand(cards: str):
    card_count = {}
    for card in cards:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    
    sorted_count = sorted(card_count.values(), reverse=True)
    
    if sorted_count[0] == 5:
        return 7  # 5 of a kind
    
    if sorted_count[0] == 4:
        return 6  # 4 of a kind
    
    if sorted_count[0] == 3:
        if sorted_count[1] == 2:
            return 5  # full house
        return 4  # 3 of a kind
    
    if sorted_count[0] == 2:
        if sorted_count[1] ==2:
            return 3  # 2 pair
        return 2  # pair
    
    return 1  # high card

card_to_number = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}
            

with open("day7.txt", "r") as file:
    lines = [line.strip().split() for line in file.readlines()]
    print(lines)
    final_inputs = {}
    for line in lines:
        converted_input = int(find_hand(line[0]))
        for card in line[0]:
            converted_input *= 100
            converted_input += card_to_number[card]

        final_inputs[converted_input] = line[1]

    final_sorted = dict(sorted(final_inputs.items()))
    print(f"sorted: {final_sorted}")
    total = 0
    for index, final in enumerate(final_sorted.values()):
        total += int(final) * (index + 1)

        print(f"total: {total}")