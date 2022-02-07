from itertools import combinations

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)
    ls = list(combinations(dices,2))
    dd = list()
    cc = list()
    ddd = dict()
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
            dd.append((y,x))
        elif d2_wins > d1_wins:
            cc.append(y)
            dd.append((x,y))
        else:
            continue
    d = max(cc, key = cc.count)
    if cc.count(d) == len(dices)-1:
        for i in range(len(dices)):
            if dices[i] == d:
                ddd['choose_first'] = ddd.get('choose_first',True)
                ddd['first_dice'] = ddd.get('first_dice',0) + i
                return ddd
    else:
        ddd['choose_first'] = ddd.get('choose_first',False)
        for i,j in dd:
            for k in range(len(dices)):
                if dices[k] == i:
                    i = k
                elif dices[k] == j:
                    j = k
            ddd[i] = j
        return ddd

dices = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
print(find_the_best_dice(dices))
