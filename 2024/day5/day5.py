def day5_p1():
    file = open("aocd5_input.txt", 'r')  # open('aocd4_input.txt', 'r')
    data = file.read().split('\n\n')

    rules = data[0].split('\n')
    rules = [list(map(int, _.split('|'))) for _ in rules]

    rules_0 = [_[0] for _ in rules]
    rules_1 = [_[1] for _ in rules]

    updates = data[1].split('\n')
    updates = [list(map(int, _.split(','))) for _ in updates]

    mid_corr_nums = []
    for i in range(len(updates)):
        correct = True
        for j in range(len(updates[i])):
            if updates[i][j] in rules_0:
                paired_ind = [_ for _, x in enumerate(rules_0) if x == updates[i][j]]
                for l in paired_ind:
                    for k in range(0, j):
                        if updates[i][k] == rules_1[l]:
                            correct = False
                            break

            if updates[i][j] in rules_1:
                paired_ind = [_ for _, x in enumerate(rules_1) if x == updates[i][j]]
                for l in paired_ind:
                    for k in range(j + 1, len(updates[i])):
                        if updates[i][k] == rules_0[l]:
                            correct = False
                            break

        if correct:
            mid_corr_nums.append(updates[i][len(updates[i])//2])

    return sum(mid_corr_nums)


def day5_p2():
    file = open("aocd5_input.txt", 'r')  # open('aocd4_input.txt', 'r')
    data = file.read().split('\n\n')

    rules = data[0].split('\n')
    rules = [list(map(int, _.split('|'))) for _ in rules]

    rules_0 = [_[0] for _ in rules]
    rules_1 = [_[1] for _ in rules]

    updates = data[1].split('\n')
    updates = [list(map(int, _.split(','))) for _ in updates]

    incorrect_updates = []
    for i in range(len(updates)):
        correct = True
        for j in range(len(updates[i])):
            incorrect_nums = []

            if updates[i][j] in rules_0:
                paired_ind = [_ for _, x in enumerate(rules_0) if x == updates[i][j]]
                for l in paired_ind:
                    for k in range(0, j):
                        if updates[i][k] == rules_1[l]:
                            updates[i][k], updates[i][j] = updates[i][j], updates[i][k]
                            # incorrect_nums.append(k)
                            correct = False

            if updates[i][j] in rules_1:
                paired_ind = [_ for _, x in enumerate(rules_1) if x == updates[i][j]]
                for l in paired_ind:
                    for k in range(j, len(updates[i])):
                        if updates[i][k] == rules_0[l]:
                            updates[i][k], updates[i][j] = updates[i][j], updates[i][k]
                            # incorrect_nums.append(k)
                            correct = False

            # print(incorrect_nums)

            # if len(incorrect_nums) > 0:
            #     updates[i][max(incorrect_nums)], updates[i][j] = updates[i][j], updates[i][max(incorrect_nums)]

        if not correct:
            incorrect_updates.append(updates[i])

    incorrect_sum_mids = 0

    for i in range(len(incorrect_updates)):
        incorrect_sum_mids += incorrect_updates[i][len(incorrect_updates[i])//2]

    return incorrect_sum_mids


if __name__ == '__main__':
    print(day5_p1())
    print(day5_p2())