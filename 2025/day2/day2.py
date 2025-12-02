def preprocess():
    file = open('aocd2_input.txt', 'r')
    data = file.read()

    d_list = data.split(',')
    d_list = [list(map(int, _.split('-'))) for _ in d_list]

    return d_list

def part_1(d_list):
    invalid = []
    for _ in d_list:
        for num in range(_[0], _[1]+1):
            str_num = str(num)
            len_str = len(str_num)
            if len_str % 2 == 0:
                first_half = str_num[0:len_str // 2]
                second_half = str_num[len_str // 2:]
                if first_half == second_half:
                    invalid.append(num)

    return sum(invalid)


if __name__ == '__main__':
    print(preprocess())
    print(part_1(preprocess()))