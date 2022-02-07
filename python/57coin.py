ls = list()
x = int(input())

count_5 = 0
while True:
    if x % 7 != 0:
        x -= 5
        count_5 += 1
        continue
    else:
        y = int(x/7)
        break

ls += count_5*[5] + y*[7]
print(ls)
