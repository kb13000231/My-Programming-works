# cook your dish here
t = input()
for i in range(int(t)):
    act_org = input()
    act, org = act_org.split()
    act = int(act)
    tot_p = 0
    for i in range(act):
        x = input()
        y = x.split()
        if y[0] == 'CONTEST_WON':
            if int(y[1]) < 20:
                p = 300 + 20 - int(y[1])
            else:
                p = 300
            tot_p += p

        elif y[0] == 'TOP_CONTRIBUTOR':
            tot_p += 300

        elif y[0] == 'BUG_FOUND':
            tot_p += int(y[1])

        elif y[0] == 'CONTEST_HOSTED':
            tot_p += 50

    if org == 'INDIAN':
        print(tot_p//200)
    else:
        print(tot_p//400)
