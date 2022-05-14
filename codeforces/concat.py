for _ in range(int(input())):
    s = input()
    c_a = 0
    c_b = 0
    ans = True

    for i in range(len(s)):
        if s[i] == 'a':
            if c_b == 1:
                ans = False
                break
            c_b = 0
            c_a += 1
        if s[i] == 'b':
            if c_a == 1:
                ans = False
                break
            c_a = 0
            c_b += 1
    print(ans)