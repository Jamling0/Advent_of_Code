def preprocess():
    file = open('aocd4.txt', 'r')
    data = file.read()

    d_list = data.split('\n')

    d2_list = []
    for i in d_list:
        s_colon_idx = i.find(':')
        d2_list.append(i[s_colon_idx + 2::])

    d3_list = []
    for j in d2_list:
        d3_list.append(j.split('|'))

    d4_list = []
    for k in d3_list:
        inner_list = []
        for l in k:
            inner_list.append(l.split(' '))
        d4_list.append(inner_list)

    for i in range(len(d4_list)):
        for j in range(len(d4_list[i])):
            d4_list[i][j] = [k for k in d4_list[i][j] if k != '']

    for i in range(len(d4_list)):
        for j in range(len(d4_list[i])):
            for k in range(len(d4_list[i][j])):
                d4_list[i][j][k] = int(d4_list[i][j][k])

    return d4_list


def pt1():
    d_list = preprocess()

    total_points = 0
    for card_num in range(len(d_list)):
        card_points = 0
        card_power = 0
        for win_nums in range(len(d_list[card_num][0])):
            if d_list[card_num][0][win_nums] in d_list[card_num][1]:
                if card_points == 0:
                    card_points += 1
                else:
                    card_points *= 2
                card_power += 1

        total_points += card_points

    return total_points


def pt2():
    d_list = preprocess() # [[[__, __, __, __, __], [__, __, __, __, __]], ...]

    new_list = []
    for cards in range(len(d_list)):
        new_list.append([d_list[cards]])

    inst_ctr = len(new_list)
    for cards_1 in range(len(new_list)):
        for card_copies in range(len(new_list[cards_1])):
            no_wins = 1
            for nums in range(len(new_list[cards_1][card_copies][0])):
                if new_list[cards_1][card_copies][0][nums] in new_list[cards_1][card_copies][1]:
                    inst_ctr += 1
                    new_list[cards_1 + no_wins].append(new_list[cards_1 + no_wins][0])
                    no_wins += 1

    return inst_ctr


if __name__ == '__main__':
    print(preprocess())
    print(pt1())
    print(pt2())
