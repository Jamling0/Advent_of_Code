def preprocess():
    hands = open('aocd7.txt', 'r').read().split('\n')
    hands = [_.split(' ') for _ in hands]
    hands = [[_[0], int(_[1])] for _ in hands]

    return hands


def pt1():
    hand_bids = preprocess()

    card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    for hand in range(len(hand_bids)):
        for hand_compare in range(hand + 1, len(hand_bids)):
            ctr = 0
            while ctr < len(hand_bids[hand][0]):
                if card_order.index(hand_bids[hand][0][ctr]) < card_order.index(hand_bids[hand_compare][0][ctr]):
                    hand_bids[hand_compare], hand_bids[hand] = hand_bids[hand], hand_bids[hand_compare]
                    break
                elif card_order.index(hand_bids[hand][0][ctr]) > card_order.index(hand_bids[hand_compare][0][ctr]):
                    break
                else:
                    ctr += 1

    hand_equals = []
    for hand_2 in range(len(hand_bids)):
        hand_crd_ctr = [0] * 13
        for card_2 in range(len(hand_bids[hand_2][0])):
            hand_crd_ctr[card_order.index(hand_bids[hand_2][0][card_2])] += 1

        hand_equals.append(hand_crd_ctr)

    for h in range(len(hand_equals)):
        if max(hand_equals[h]) == 2:
            if hand_equals[h].count(2) == 2:
                hand_bids[h][0] = 2
            else:
                hand_bids[h][0] = 1
        elif max(hand_equals[h]) == 3:
            if 2 in hand_equals[h]:
                hand_bids[h][0] = 4
            else:
                hand_bids[h][0] = 3
        elif max(hand_equals[h]) == 4:
            hand_bids[h][0] = 5
        elif max(hand_equals[h]) == 5:
            hand_bids[h][0] = 6
        else:
            hand_bids[h][0] = 0

    hand_bids = sorted(hand_bids, key=lambda hand: hand[0])

    final_score = 0
    for k in range(len(hand_bids)):
        final_score += hand_bids[k][1] * (k + 1)

    return final_score


def pt2():
    hand_bids = preprocess()

    card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

    for hand in range(len(hand_bids)):
        for hand_compare in range(hand + 1, len(hand_bids)):
            ctr = 0
            while ctr < len(hand_bids[hand][0]):
                if card_order.index(hand_bids[hand][0][ctr]) < card_order.index(hand_bids[hand_compare][0][ctr]):
                    hand_bids[hand_compare], hand_bids[hand] = hand_bids[hand], hand_bids[hand_compare]
                    break
                elif card_order.index(hand_bids[hand][0][ctr]) > card_order.index(hand_bids[hand_compare][0][ctr]):
                    break
                else:
                    ctr += 1

    hand_equals = []
    for hand_2 in range(len(hand_bids)):
        hand_crd_ctr = [0] * 13
        for card_2 in range(len(hand_bids[hand_2][0])):
            hand_crd_ctr[card_order.index(hand_bids[hand_2][0][card_2])] += 1

        hand_equals.append(hand_crd_ctr)

    for hand in range(len(hand_equals)):
        if hand_equals[hand][-1] > 0:
            highest_non_jkr = hand_equals[hand].index(max(hand_equals[hand][0:12]))
            hand_equals[hand][highest_non_jkr] += hand_equals[hand][-1]
            hand_equals[hand][-1] = 0

    for h in range(len(hand_equals)):
        if max(hand_equals[h]) == 2:
            if hand_equals[h].count(2) == 2:
                hand_bids[h][0] = 2
            else:
                hand_bids[h][0] = 1
        elif max(hand_equals[h]) == 3:
            if 2 in hand_equals[h]:
                hand_bids[h][0] = 4
            else:
                hand_bids[h][0] = 3
        elif max(hand_equals[h]) == 4:
            hand_bids[h][0] = 5
        elif max(hand_equals[h]) == 5:
            hand_bids[h][0] = 6
        else:
            hand_bids[h][0] = 0

    hand_bids = sorted(hand_bids, key=lambda hand: hand[0])

    final_score = 0
    for k in range(len(hand_bids)):
        final_score += hand_bids[k][1] * (k + 1)

    return final_score


if __name__ == '__main__':
    print(preprocess())
    # print(pt1())
    print(pt2())
