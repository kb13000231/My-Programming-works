from itertools import combinations

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    ls = list(combinations(dices,2))
    dd = list()
    cc = list()
    for x,y in ls:
        d1_wins = 0
        d2_wins = 0
        for i in x:
            for j in y:
                if i>j:
                    d1_wins += 1
                elif j>i:
                    d2_wins += 1
                else:
                    continue
        if d1_wins > d2_wins:
            cc.append(x)
        elif d2_wins > d1_wins:
            cc.append(y)
        else:
            continue
    d = max(cc, key = cc.count)
    if cc.count(d) == len(dices)-1:
        for i in range(len(dices)):
            if dices[i] == d:
                return i
    else:
        return -1

dices = [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
print(find_the_best_dice(dices))
