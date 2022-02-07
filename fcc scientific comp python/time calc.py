def add_time(start, duration, day=None):
    start = start.split()
    sh, sm = list(map(int, start[0].split(":")))
    dh, dm = list(map(int, duration.split(":")))
    st = 0 if start[1] == 'AM' else 1

    nm = sm + dm
    nh = sh + dh if nm//60 == 0 else sh + dh + 1
    nm = nm if nm//60 == 0 else nm % 60
    nm = str(nm) if nm >= 10 else '0'+str(nm)
    n = int(st)

    if nh >= 12:
        if (nh//12) % 2 != 0:
            st = 0 if st == 1 else 1
            n += nh//12
            nh = nh % 12
            nh = 12 if nh == 0 else nh
    mer = "AM" if st == 0 else 'PM'
    new_time = str(nh) + ":" + nm + ' '+mer

    if day is None:
        if n//2 > 0:
            nd = n//2
            if nd == 1:
                return new_time + ' (next day)'
            else:
                return new_time + ' ({} days later)'.format(nd)
        else:
            return new_time
    else:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = day.lower()
        ind_day = days.index(day)
        ind_day = (ind_day + (n//2)) % 7
        day = days[ind_day].capitalize()
        if n//2 > 0:
            nd = n//2
            if nd == 1:
                return new_time + ', ' + day + ' (next day)'
            else:
                return new_time + ', ' + day + ' ({} days later)'.format(nd)
        else:
            return new_time + ', ' + day
