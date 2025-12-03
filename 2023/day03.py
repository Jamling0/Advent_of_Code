def preprocess():
    file = open('aocd3.txt', 'r')
    data = file.read()

    d_list = data.split('\n')

    d1_list = []
    for i in d_list:
        inner_list = []
        for j in i:
            inner_list.append(j)
        d1_list.append(inner_list)

    return d1_list


def pt1():
    d_list = preprocess()

    symbols = ['*', '#', '+', '$', '=', '/', '&', '%', '@', '!', '^', '(', ')', '-']

    simp_list = []
    symbol_list = []
    last_num = 0
    inner_list = ['', 0, []]
    for i in range(len(d_list)):
        for j in range(len(d_list[i])):
            if d_list[i][j] in symbols:
                symbol_list.append((i, j))
            if last_num == 1 and d_list[i][j] != '.' and d_list[i][j] not in symbols:
                inner_list[0] += d_list[i][j]
                inner_list[2].append(j)
            elif d_list[i][j].isnumeric():
                last_num = 1
                inner_list[0] += d_list[i][j]
                inner_list[1] += i
                inner_list[2].append(j)
            elif last_num and (d_list[i][j] == '.' or d_list[i][j] in symbols):
                last_num = 0
                simp_list.append(inner_list)
                inner_list = ['', 0, []]

    # making the numbers ints
    for m in simp_list:
        m[0] = int(m[0])

    # testing the symbol locations
    list_engine_pts = []
    sum_engine_pts = 0
    for sym_loc in symbol_list:
        for num_data in simp_list:
            include = 0
            if sym_loc[0] - 1 <= num_data[1] <= sym_loc[0] + 1:
                for col in num_data[2]:
                    if sym_loc[1] - 1 <= col <= sym_loc[1] + 1:
                        include = 1

            if include:
                list_engine_pts.append(num_data[0])
                sum_engine_pts += num_data[0]

    return sum_engine_pts, list_engine_pts


def pt2():
    d_list = preprocess()

    symbols = ['*']
    other_symbols = ['*', '#', '+', '$', '=', '/', '&', '%', '@', '!', '^', '(', ')', '-']

    simp_list = []
    symbol_list = []
    last_num = 0
    inner_list = ['', 0, []]
    for i in range(len(d_list)):
        for j in range(len(d_list[i])):
            if d_list[i][j] in symbols:
                symbol_list.append((i, j))
            if last_num == 1 and d_list[i][j] != '.' and d_list[i][j] not in other_symbols:
                inner_list[0] += d_list[i][j]
                inner_list[2].append(j)
            elif d_list[i][j].isnumeric():
                last_num = 1
                inner_list[0] += d_list[i][j]
                inner_list[1] += i
                inner_list[2].append(j)
            elif last_num and (d_list[i][j] == '.' or d_list[i][j] in symbols):
                last_num = 0
                simp_list.append(inner_list)
                inner_list = ['', 0, []]

    for m in simp_list:
        m[0] = int(m[0])

    list_engine_pts = []
    sum_engine_pts = 0
    for sym_loc in symbol_list:
        ctr = 0
        nums = 1
        for num_data in simp_list:
            include = 0
            if sym_loc[0] - 1 <= num_data[1] <= sym_loc[0] + 1:
                for col in num_data[2]:
                    if sym_loc[1] - 1 <= col <= sym_loc[1] + 1:
                        include = 1

            if include:
                ctr += 1
                nums *= num_data[0]

        if ctr == 2:
            list_engine_pts.append(nums)
            sum_engine_pts += nums

    return sum_engine_pts, list_engine_pts





if __name__ == '__main__':
    preprocess()
    print(pt1())
    print(pt2())