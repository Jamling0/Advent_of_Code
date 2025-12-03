def preprocess():
    seqs = open('aocd9.txt', 'r').read().split('\n')
    seqs = [list(map(int, _.split())) for _ in seqs]

    return seqs


def pt1():
    seqs = preprocess()

    pred_nums = []
    for seq in seqs:
        seq_layers = [seq]
        while seq_layers[-1].count(0) != len(seq_layers[-1]):
            ctr = 0
            seq_layers.append([])
            while ctr < len(seq_layers[-2]) - 1:
                seq_layers[-1].append(seq_layers[-2][ctr+1] - seq_layers[-2][ctr])
                ctr += 1

        count_up = 0
        for i in range(len(seq_layers)):
            if len(seq_layers[i]) != 0:
                count_up += seq_layers[i][-1]
            else:
                count_up += 0

        pred_nums.append(count_up)

    return sum(pred_nums)


def pt2():
    seqs = preprocess()

    pred_nums = []
    for seq in seqs:
        seq_layers = [seq[::-1]]
        while seq_layers[-1].count(0) != len(seq_layers[-1]):
            ctr = 0
            seq_layers.append([])
            while ctr < len(seq_layers[-2]) - 1:
                seq_layers[-1].append(seq_layers[-2][ctr + 1] - seq_layers[-2][ctr])
                ctr += 1

        count_up = 0
        for i in range(len(seq_layers)):
            if len(seq_layers[i]) != 0:
                count_up += seq_layers[i][-1]
            else:
                count_up += 0

        pred_nums.append(count_up)

    return sum(pred_nums)


if __name__ == '__main__':
    print(preprocess())
    print(pt1())
    print(pt2())
