def preprocess():
    file = open('aocd1_input.txt', 'r')
    data = file.read()
    
    d_list = data.split()

    return d_list

def pt_1(d_list):

    dial_pos = 50
    zero_ctr = 0

    for i in d_list:
        if str(i)[0] == 'R':
            dial_pos = (dial_pos + int(i[1:])) % 100
        else:
            dial_pos = (dial_pos - int(i[1:])) % 100

        if dial_pos == 0:
            zero_ctr += 1

    return zero_ctr

def pt_2(d_list):
    dial_pos = 50
    zero_ctr = 0

    for instr in d_list:
        old_dial_pos = 0
        old_dial_pos += dial_pos
        instr_dir = instr[0]
        instr_num = int(instr[1:])

        # more than 100 will definitely pass 0
        num_spins = instr_num // 100
        zero_ctr += num_spins

        if instr_dir == 'R':
            dial_pos = (dial_pos + instr_num) % 100
            if old_dial_pos > dial_pos:
                zero_ctr += 1
        else:
            dial_pos = (dial_pos - instr_num) % 100
            if old_dial_pos != 0:
                if dial_pos == 0 and old_dial_pos != 0:
                    zero_ctr += 1
                elif old_dial_pos < dial_pos:
                    zero_ctr += 1


    return zero_ctr

if __name__ == '__main__':
    instr_list = preprocess()
    print(pt_1(instr_list))
    print(pt_2(instr_list))
    