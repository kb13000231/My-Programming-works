for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if n < 3:
        print('YES')
    else:
        coun = 0
        # ans = True

        for i in range(n-1):
            if arr[i] > arr[i+1]:
                coun += 1
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                if i > 0:
                    if arr[i] < arr[i-1]:
                        coun += 1
                        break
                if coun > 1:
                    break

        if coun > 1:
            print('NO')
        else:
            print('YES')
