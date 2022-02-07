def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    ls = list()
    dd = list()
    for i in range(len(dices)):
        d1_wins = 0
        d2_wins = 0
        for j in dices[i]:
            if i<len(dices)-1:
                for k in dices[i+1]:
                    if j>k:
                        d1_wins += 1
                    elif k>j:
                        d2_wins += 1
                    else:
                        continue
            else:
                for k in dices[0]:
                    if j>k:
                        d1_wins += 1
                    elif k>j:
                        d2_wins += 1
                    else:
                        continue
        ls.append((d1_wins,d2_wins))
        if d1_wins > d2_wins:
            dd.append(i)
        elif d1_wins == d2_wins:
            continue
        else:
            if i <len(dices)-1:
                dd.append(i+1)
            else:
                dd.append(0)
    c = 0
    a = 0
    for x,y in ls:
        if x>y:
            c += 1
        elif y>x:
            a += 1
    if c == len(dices) or a == len(dices):
        return -1
    else:
        return max(dd,key=dd.count)


dices = [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]
print(find_the_best_dice(dices))







#    dice1_wins = 0
#    dice2_wins = 0
#    dice3_wins = 0
#    for i in dice[0]:
#        for j in dice[1]:
#            if i>j:
#                dice1_wins += 1
#            elif j>i:
#                dice2_wins += 1
#            else:
#                continue
