import math


def preprocess():
    file = open('aocd2.txt', 'r')
    data = file.read()

    d_list = data.split('\n')

    d2_list = []
    for i in d_list:
        s_colon_idx = i.find(':')
        d2_list.append(i[s_colon_idx+2::])

    d3_list = []
    for j in d2_list:
        d3_list.append(j.split(';'))

    d4_list = []
    for l in d3_list:
        inner_list = []
        for k in l:
            inner_list.append((k.strip()).split(','))
        d4_list.append(inner_list)

    d5_list = []
    for m in d4_list:
        inner_list1 = []
        for n in m:
            inner_list2 = []
            for g in n:
                g = g.strip()
                inner_list2.append(g.split(' '))
            inner_list1.append(inner_list2)
        d5_list.append(inner_list1)

    return d5_list


def pt1():
    d_list = preprocess()

    acceptable_digits = [12, 13, 14]
    # [R, G, B]

    possible_games = [1] * len(d_list)
    for i in range(len(d_list)): # games
        for j in d_list[i]: # selections with replacement i.e j: [['3', 'blue'], ['4', 'red']]
            game_break = 0
            for k in j: # k: ['3', 'blue']
                if k[1][0] == 'r' and int(k[0]) > acceptable_digits[0]:
                    possible_games[i] -= 1
                    game_break += 1
                    break
                elif k[1][0] == 'g' and int(k[0]) > acceptable_digits[1]:
                    possible_games[i] -= 1
                    game_break += 1
                    break
                elif k[1][0] == 'b' and int(k[0]) > acceptable_digits[2]:
                    possible_games[i] -= 1
                    game_break += 1
                    break

            if game_break:
                break

    game_sum = 0
    for m in range(len(possible_games)):
        if possible_games[m]:
            game_sum += m+1

    return game_sum


def pt2():
    d_list = preprocess()

    min_colour_games = []
    for i in range(len(d_list)): # game
        min_colours = [0, 0, 0]
        for j in d_list[i]: # round
            for k in j: # colour
                if k[1][0] == 'r' and int(k[0]) > min_colours[0]:
                    min_colours[0] = int(k[0])
                elif k[1][0] == 'g' and int(k[0]) > min_colours[1]:
                    min_colours[1] = int(k[0])
                elif k[1][0] == 'b' and int(k[0]) > min_colours[2]:
                    min_colours[2] = int(k[0])

        min_colour_games.append(math.prod(min_colours))

    return sum(min_colour_games)


if __name__ == '__main__':
    print(preprocess())
    print(pt1())
    print(pt2())