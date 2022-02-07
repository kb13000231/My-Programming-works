ls = list()
c_5, c_7 = 0, 0


def change(amount, ls):
    global c_5
    global c_7
    if amount % 7 != 0:
        amount -= 5
        c_5 += 1
        ls.append(5)
        change(amount)
        return ls
    else:
        c_7 = amount//7
        ls += c_7*[7]
        return ls


change(int(input()), ls)
print('5 coins:', c_5, '7 coins:', c_7)
