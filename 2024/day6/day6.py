def day6_p1():
    file = open("example.txt", 'r')  # open('aocd4_input.txt', 'r')
    guard_map = file.read().split('\n')

    for i in range(len(guard_map)):
        for j in range(len(guard_map[i])):
                if guard_map[i][j] == '^':
                    start_col = j
                    start_row = i

    tick = True
    curr_col = start_col
    curr_row = start_row
    guard_dir = '^'

    unique_pos_sum = 0
    cols_traversed = []
    rows_traversed = []

    while tick:
        if guard_dir == '^':
            for i in range(curr_row, 0):
                if guard_map[i][curr_col] == '#':
                    unique_pos_sum += curr_row - i
                    curr_row = i + 1
                    guard_dir = '>'
                else:
                    tick = False
                    unique_pos_sum += curr_row - i
        elif guard_dir == '>':
            for i in range(curr_col, len(guard_map[curr_row])):
                if guard_map[curr_row][i] == '#':
                    unique_pos_sum += len(guard_map[0]) - curr_col
                    curr_col = i - 1
                    guard_dir = 'V'
                else:
                    tick = False
                    unique_pos_sum += len(guard_map[0]) - curr_col
        elif guard_dir == 'V':
            for i in range(curr_row, len(guard_map)):
                if guard_map[i][curr_col] == '#':
                    unique_pos_sum += curr_row - i
                    curr_row = i - 1




    print(guard_map)


if __name__ == '__main__':
    print(day6_p1())