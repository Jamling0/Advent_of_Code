def preprocess():
    file = open('aocd5.txt', 'r')
    data = file.read()

    d_list = data.split('\n')

    s_colon_idx = d_list[0].find(':')
    d_list[0] = d_list[0][s_colon_idx + 2::]

    ctr = 1
    mem = 1
    inner_ctr = 0
    new_list = []
    new_list.append(d_list[0].split(' '))
    while ctr < len(d_list):
        if d_list[ctr] == '':
            inner_ctr += 1
            ctr += 2
            mem = 1
        elif mem == 1:
            new_list.append([])
            new_list[inner_ctr].append(d_list[ctr].split(' '))
            mem += 1
            ctr += 1
        elif mem > 1:
            new_list[inner_ctr].append(d_list[ctr].split(' '))
            ctr += 1

    for i in range(len(new_list[0])):
        new_list[0][i] = int(new_list[0][i])

    for i in range(1, len(new_list)):
        for j in range(len(new_list[i])):
            for k in range(len(new_list[i][j])):
                new_list[i][j][k] = int(new_list[i][j][k])

    return new_list


def p1():
    d_list = preprocess()

    seed_maps = []
    for i in range(len(d_list[0])):
        leading_num = d_list[0][i]
        for j in range(1, len(d_list)):
            for k in range(len(d_list[j])):
                if d_list[j][k][1] <= leading_num < d_list[j][k][1] + d_list[j][k][2]:
                    leading_num = d_list[j][k][0] + (leading_num - d_list[j][k][1])
                    break

        seed_maps.append(leading_num)

    return min(seed_maps)


def p2():
    d_list = preprocess()

    new_seeds = []
    ctr = 0
    while ctr < len(d_list[0]):
        new_seeds.append(range(d_list[0][ctr], d_list[0][ctr] + d_list[0][ctr + 1]))
        ctr += 2

    d_list[0] = new_seeds

    loca_num = 0
    seed_num = 0
    ctr = 0
    breaker = 0
    while True:
        loca_num = seed_num
        for j in range(len(d_list) - 1, 0, -1):
            for k in range(len(d_list[j])):
                if d_list[j][k][0] <= seed_num < d_list[j][k][0] + d_list[j][k][2]:
                    seed_num = d_list[j][k][1] + (seed_num - d_list[j][k][0])
                    break
        for i in d_list[0]:
            if seed_num in i:
                breaker = 1
                break
        if breaker:
            break
        seed_num = ctr + 1
        ctr += 1

    return loca_num




if __name__ == '__main__':
    print(preprocess())
    print(p1())
    print(p2())
