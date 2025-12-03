def preprocess():
    file = open('aocd1_input.txt', 'r')
    data = file.read()

    d_list = data.split()
    return d_list


def pt1():
    d_list = preprocess()

    output_list = []
    for i in d_list:
        out = []
        for j in range(len(i)):
            if i[j].isnumeric():
                out.append(i[j])
                break

        for k in range(len(i) -1, -1, -1):
            if i[k].isnumeric():
                out.append(i[k])
                break

        output_list.append(int(out[0] + out[1]))

    return sum(output_list)


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)


def pt2():
    d_list = preprocess()

    valid_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    output_list = []

    for i in d_list:
        out = []
        for j in range(len(i)):
            if i[j].isnumeric():
                out.append(i[j])
                break

        if len(out) == 0:
            out.append(str(1))

        for k in range(len(i) - 1, -1, -1):
            if i[k].isnumeric():
                out.append(i[k])
                break

        if len(out) == 1:
            out.append(str(1))

        # forward
        written_inds = []
        for l in valid_digits:
            found_nums = list(find_all(i, l))
            for h in found_nums:
                written_inds.append(h)
            # if i.find(l) != -1:
            #     written_inds.append(i.find(l))

        if len(written_inds) != 0:

            written_num = 0
            iterator = min(written_inds)
            min_written_ind = min(written_inds)
            for b in range(len(valid_digits)):
                iterator = min(written_inds)
                for x in range(len(valid_digits[b])):
                    if i[iterator] != valid_digits[b][x]:
                        break
                    iterator += 1
                if x > 1:
                    written_num = b + 1
                    break

            if min_written_ind < j:
                out[0] = str(written_num)

            # reverse
            # written_inds = []
            # for l in valid_digits:
            #     if i.find(l) != -1:
            #         written_inds.append(i.find(l))

            written_num_rev = 0
            max_written_ind = max(written_inds)
            for a in range(len(valid_digits)):
                iterator_0 = max(written_inds)
                for z in range(len(valid_digits[a])):
                    if i[iterator_0] != valid_digits[a][z]:
                        break
                    if iterator_0 != len(i) - 1:
                        iterator_0 += 1
                if z > 1:
                    written_num_rev = a + 1
                    break

            if max_written_ind > k:
                out[1] = str(written_num_rev)

        output_list.append(int(out[0] + out[1]))

    return sum(output_list)


if __name__ == '__main__':
    preprocess()
    # print(pt1())
    print(pt2())