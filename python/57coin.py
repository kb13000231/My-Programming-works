def coins57(amt):
    ls_req = [3, 6, 2, 5, 8, 3]
    remain = amt % 7
    c5 = ls_req[remain - 1] if remain != 0 else 0
    if amt < c5 * 5:
        return 'Invalid input'
    c7 = (amt - c5 * 5)//7
    ls = [5]*c5 + [7]*c7
    return ls


amt = int(input())
print(coins57(amt))
