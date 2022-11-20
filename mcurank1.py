def add_item(k, items, final):
    if len(final) == 0:
        final.append(items[k])
    
    else:
        l, r = 0, len(final)-1
        while l <= r:
            mid = (l+r)//2
            new_add = input(f"Which would you like to watch: {items[k]} or {items[mid]}? Enter 1 Or 2: ")
            if new_add == "1":
                r = mid-1
            else:
                l = mid+1
        final.insert(l, items[k])


items = ["Iron Man", "The Incredible Hulk", "Iron Man 2", "Thor", "Captain America:The First Avenger", "Avengers"]
items += ["Iron Man 3", "Thor: The dark world", "Captain America: The Winter Soldier", "Guardians of the Galaxy", "Avengers: Age of Ultron", "Ant Man"]
items += ["Captain America: Civil War", "Doctor Strange", "Guardians of the Galaxy Vol 2", "Spider-man Homecoming", "Thor: Ragnarok"]
items += ["Black Panther", "Avengers: Infinity War", "Ant man and the Wasp", "Captain Marvel", "Avengers: Endgame"]
items += ["Spider-man Far From Home", "Wandavision", "Falcon and the Winter Soldier", "Loki","Black Widow", "What if?", "Shang-Chi and the Legend of the Ten Rings"]
items += ["Eternals", "Hawkeye", "Spider-man No Way Home", "Moon Knight", "Doctor Strange in the Multiverse of Madness", "Ms. Marvel"]
items += ["Thor: Love and Thunder", "I am Groot", "She-Hulk",  "WereWolf by Night", "Black Panther:Wakanda Forever"]

print(len(items))
items2 = items[:23] + items[26] + items[28:30] + items[31] + items[33] + items[35] + items[39]

sel = input("Only movies or movies + shows? Enter 1 or 2: ")

if sel == "1":
    items = items2

final = []
n = len(items)

for i in range(n):
    add_item(i, items, final)

with open("rank.txt", "w") as f:
    for i in final:
        f.write(f"{final.index(i)+1}: {i}\n")