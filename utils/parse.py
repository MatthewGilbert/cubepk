# parse file from http://www.randomwalk.de/sequences/a084824.txt
# add generate a coor.py file which contains a list of the best
# coordinate locations.


with open('a084824.txt') as f:
    lines = f.readlines()
    # ignore pre coordinate information
    lines = lines[142:]

count = 0
locations = []
coords = []

for line in lines:
    parts = line.split()
    # get number of lines to parse into dictionary
    if not parts:
        continue
    elif count == 0:
        count = int(parts[0])
        locations.append(coords)
        coords = []
    else:
        count -= 1
        coords.append(map(float, parts[1:]))
locations.append(coords)
locations = locations[1:]

with open('coord.py', 'w') as f:
    f.write("_coords = [\n")
    for item in locations:
        f.write("%s,\n" % item)
    f.seek(-2, 1)
    f.write("\n]")
