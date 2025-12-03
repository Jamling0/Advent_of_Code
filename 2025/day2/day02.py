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

def part_2(d_list):
    invalid = []
    for ids in d_list:
        for num in range(ids[0], ids[1]+1):
            str_num = str(num)
            len_str = len(str_num)
            for divisible in range(1, len_str // 2 + 1):
                if len(str_num) % divisible == 0:
                    # len_group = len(str_num) // divisible
                    num_ptr = 0
                    test_groups = []
                    while num_ptr < len_str:
                        test_groups.append(str_num[num_ptr:divisible + num_ptr])
                        num_ptr += divisible
                    if len(set(test_groups)) == 1:
                        invalid.append(num)
                        break

    return sum(invalid)



if __name__ == '__main__':
    print(preprocess())
    print(part_1(preprocess()))
    print(part_2(preprocess()))