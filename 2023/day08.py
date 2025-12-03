import math


def preprocess():
    movement, *nodes = open('aocd8.txt', 'r').read().split('\n\n')
    nodes = nodes[0].split('\n')

    nodes = [_.split(' = ') for _ in nodes]

    nodes = [[_[0], _[1].strip('(').strip(')').split(', ')] for _ in nodes]

    return movement, nodes


def pt1():
    movement, nodes = preprocess()

    node_list = [_[0] for _ in nodes]
    current_node = node_list.index('AAA')
    lr_ptr = 0
    steps = 0
    while node_list[current_node] != 'ZZZ':
        if movement[lr_ptr] == 'L':
            current_node = node_list.index(nodes[current_node][1][0])
            if lr_ptr + 1 == len(movement):
                lr_ptr = 0
            else:
                lr_ptr += 1
            steps += 1
        else:
            current_node = node_list.index(nodes[current_node][1][1])
            if lr_ptr + 1 == len(movement):
                lr_ptr = 0
            else:
                lr_ptr += 1
            steps += 1

    return steps


def pt2():
    movement, nodes = preprocess()

    node_list = [_[0] for _ in nodes]
    current_nodes = []
    [current_nodes.append(_) for _ in range(len(node_list)) if node_list[_][2] == 'A']
    node_memory = [[] for _ in current_nodes]
    lr_ptr = 0
    steps = 0
    breaker = 0
    loop_length = [0] * len(current_nodes)

    while breaker != len(current_nodes):
        breaker = 0
        if movement[lr_ptr] == 'L':
            for node in range(len(current_nodes)):
                prospective_node = node_list.index(nodes[current_nodes[node]][1][0])
                node_memory[node].append(current_nodes[node])
                if node_list[prospective_node][2] != 'Z':
                    current_nodes[node] = prospective_node
                else:
                    # loop_start = node_memory[node].index(prospective_node)
                    if loop_length[node] == 0:
                        loop_length[node] = len(node_memory[node])
            if lr_ptr + 1 == len(movement):
                lr_ptr = 0
            else:
                lr_ptr += 1
            # steps += 1
        else:
            for node in range(len(current_nodes)):
                prospective_node = node_list.index(nodes[current_nodes[node]][1][1])
                node_memory[node].append(current_nodes[node])
                if node_list[prospective_node][2] != 'Z':
                    current_nodes[node] = prospective_node
                else:
                    # loop_start = node_memory[node].index(prospective_node)
                    if loop_length[node] == 0:
                        loop_length[node] = len(node_memory[node])
            if lr_ptr + 1 == len(movement):
                lr_ptr = 0
            else:
                lr_ptr += 1
        for i in loop_length:
            if i > 0:
                breaker += 1

    return math.lcm(loop_length[0], loop_length[1], loop_length[2], loop_length[3], loop_length[4], loop_length[5])


if __name__ == '__main__':
    print(preprocess())
    #print(pt1())
    print(pt2())
