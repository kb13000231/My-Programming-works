for _ in range(int(input())):
    s1 = ''
    s2 = input()

    if s2[0] == 'B' or s2[-1] == "A":
        print('NO')
    else:
        freq = {}
        ans = True
        for i in s2:
            freq[i] = freq.get(i, 0) + 1
            if freq['A'] < freq.get('B', 0):
                ans = False
                break
        if not ans:
            print('NO')
        else:
            print('YES')
