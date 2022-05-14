# solution is not correct

from collections import Counter as ct

for _ in range(int(input())):
    n = int(input())
    arr = input().split()

    freq = ct(arr)
    freq_list = ct.most_common(freq)
    freq_list = [i[1] for i in freq_list]

    freq_list.append(1)
    t = 1
    tot = len(arr)
    freq_list[0] -= 1
    inf = 1

    while inf < n:
        if t <= len(freq_list):
            for i in range(t-1):
                if freq_list[i] > 0:
                    freq_list[i] = freq_list[i] - 1
                    inf += 1
        else:
            freq_list2 = [i-1 for i in freq_list if i != 0]
            inf += len(freq_list2)

        if t < len(freq_list):
            freq_list[t] -= 1
            inf += 1
        else:
            if sum(freq_list) == 0:
                break
            a = freq_list.index(max(freq_list))
            freq_list[a] -= 1
            inf += 1
        t += 1
    print(t)

#  for the first second infect the node which has most siblings
#  meaning freq_list[0] -= 1
#  from second onwards till t == len(freq_list)
