# cook your dish here
def check_prime(n):
    if n%2 == 0:
        return 'NO'
    a = int(n**(1/2))
    
    for i in range(2, a + 1):
        if n%i == 0:
            return 'NO'
    return 'YES'

for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    
    if x <= n:
        if x != 1:
            print("YES")
        else:
            print("NO")
    else:
        if n % 2 == 1:
            maxval = (n//2 + 1) ** 2
            if x > maxval:
                print("NO")
            elif check_prime(n) == "YES" and x % n == 0 and x//n > 1:
                print("NO")
            else:
                if check_prime(x) == "NO":
                    print("YES")
                else:
                    print("NO")
                
        else:
            maxval = (n/2 + 1) ** 2 - (n/2 + 1)
            if x > maxval:
                print("NO")
            else:
                if check_prime(x) == "NO":
                    print("YES")
                else:
                    print('NO')