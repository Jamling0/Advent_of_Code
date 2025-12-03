import math


def preprocess():
    times, distances = open('aocd6.txt', 'r').read().split('\n')
    times = list(map(int, times.split(':')[1].split()))
    distances = list(map(int, distances.split(':')[1].split()))

    td = [times, distances]

    return td


def pt1():
    td = preprocess()

    hold_times = []
    for i in range(len(td[0])):
        hold_times.append([])

    for time in range(len(td[0])):
        for hold in range(0, td[0][time]+1):
            if hold * (td[0][time] - hold) > td[1][time]:
                hold_times[time].append(hold)

    for winning_hold in range(len(hold_times)):
        hold_times[winning_hold] = len(hold_times[winning_hold])

    return math.prod(hold_times)


def pt2():
    times, distances = open('aocd6.txt', 'r').read().split('\n')
    times = list(times.split(':')[1].strip())
    times_2 = ''
    for i in times:
        if i.isnumeric():
            times_2 += i
    distances = list(distances.split(':')[1].strip())
    distances_2 = ''
    for j in distances:
        if j.isnumeric():
            distances_2 += j

    times_2 = int(times_2)
    distances_2 = int(distances_2)

    hold_times = []
    for hold in range(0, times_2 + 1):
        if hold * (times_2 - hold) > distances_2:
            hold_times.append(hold)

    return len(hold_times)


if __name__ == '__main__':
    print(preprocess())
    print(pt1())
    print(pt2())