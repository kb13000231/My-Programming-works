def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    for i in dice1:
        for j in dice2:
            if i>j:
                dice1_wins += 1
            elif j>i:
                dice2_wins += 1
            else:
                continue
    return (dice1_wins, dice2_wins)

d1 = [1, 1, 6, 6, 8, 8]
d2 = [2, 2, 4, 4, 9, 9]

print(count_wins(d1,d2))
