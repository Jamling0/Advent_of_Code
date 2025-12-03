def preprocess():
    file = open('aocd3_input.txt', 'r')
    data = file.read()

    battery_bank = data.split()
    # battery_bank = [_.split() for _ in battery_bank]

    return battery_bank

def part_1(battery_bank):
    highest_joltage_pairs = []
    for bank in battery_bank:
        joltage_pairs = []
        for battery in range(len(bank)):
            for second_battery in range(battery + 1, len(bank)):
                joltage_pairs.append(int(bank[battery] + bank[second_battery]))
        highest_joltage_pairs.append(max(joltage_pairs))

    return sum(highest_joltage_pairs)

def part_2(battery_bank):
    highest_joltage_strings = []
    battery_bank = [list(_) for _ in battery_bank]
    for bank in range(len(battery_bank)):
        test_joltage = battery_bank[bank][(len(battery_bank[bank])-12):len(battery_bank[bank])]
        sorted_pointer = -1
        for i in range(len(test_joltage)):
            temp = [0, 0]
            for j in range(len(battery_bank[bank]) - 13 + i, sorted_pointer, -1):
                if int(battery_bank[bank][j]) >= temp[1]:
                    temp[0] = j
                    temp[1] = int(battery_bank[bank][j])
            if temp[1] >= int(test_joltage[i]):
                sorted_pointer = temp[0]
                test_joltage[i] = str(temp[1])
            else:
                sorted_pointer = len(battery_bank[bank]) - 12 + i
        highest_joltage_strings.append(test_joltage)

    actual_highest = [int(''.join(_)) for _ in highest_joltage_strings]

    return sum(actual_highest)



if __name__ == '__main__':
    print(preprocess())
    print(part_1(preprocess()))
    print(part_2(preprocess()))