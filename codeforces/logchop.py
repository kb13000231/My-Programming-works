for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    rounds = 0
    for i in arr:
        rounds += i-1

    if rounds % 2 == 0:
        print('maomao90')
    else:
        print('errorgorn')
