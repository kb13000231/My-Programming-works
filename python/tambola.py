import random

def tambola_board(ls):
    b = ''
    for i in range(90):
        z = i+1
        if z in ls:
            if z%10 == 0:
                b += ' ?\n\n'
            else:
                b += ' ?  '
        else:
            if z%10 == 0:
                b += str(z) + '\n\n'
            elif z < 10:
                b += ' ' + str(z) + '  '
            else:
                b += str(z) + '  '
    return b


ls = list()
x = list()
for i in range(90):
    ls.append(i+1)
    x.append(i+1)

print('Press Enter to play Tambola & print numbers, "done" if you are done playing and type "board" to display the board at any time')
while len(ls) > 0:
    l = input()
    if l == 'board':
        print(tambola_board(ls))
    elif l == 'done':
        break
    elif l == 'reset':
        ls = x
    else:
        a = random.choice(ls)
        ls.remove(a)
        print(a)
