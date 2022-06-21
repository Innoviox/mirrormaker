from collections import defaultdict


def find_regions(s):
    regions = defaultdict(list)
    s = s.split("\n")
    for x, line in enumerate(s):
        for y, char in enumerate(line):
            if char != '.':
                start = (x, y)
                # assume the region is right-rectangular (todo: unassume this)
                # also assume the region never hits hte edge
                a, b = x, y
                while s[a][b] == char:
                    a += 1
                a -= 1
                while s[a][b] == char:
                    b += 1
                b -= 1

                if not any(r[1] == (a, b) for r in regions[int(char)]):
                    regions[int(char)].append((start, (a, b)))
    return regions


vertices = []

with open("test_sword.txt") as f:
    s = f.read()
    for x, line in enumerate(s.split("\n")):
        for y, ch in enumerate(line):
            if ch in '123456789':
                vertices.append((x, y, int(ch)))

    regions = find_regions(s)
    print(regions)

real_vertices = []
faces = []
for v in vertices:
    # each vertex gets a square around it
    x, y, depth = v

    for d in [depth, -depth]:
        sq = [(x, y, d), (x + 1, y, d), (x, y + 1, d),
              (x + 1, y + 1, d)]  # todo z

        l = len(real_vertices)
        faces.append((l + 1, l + 2, l + 4, l + 3))

        real_vertices.extend(sq)

for depth, region in regions.items():
    for r in region:
        topleft, bottomright = r
        x1, y1 = topleft
        x2, y2 = bottomright

        # create top
        faces.append(((vertices.index((x1, y1, depth)) * 8) + 1,
                      (vertices.index((x1, y2, depth)) * 8) + 3,
                      (vertices.index((x1, y2, depth)) * 8) + 7,
                      (vertices.index((x1, y1, depth)) * 8) + 5))

        # create front
        # create back
        # create bottom
        faces.append(((vertices.index((x2, y1, depth)) * 8) + 2,
                      (vertices.index((x2, y2, depth)) * 8) + 4,
                      (vertices.index((x2, y2, depth)) * 8) + 8,
                      (vertices.index((x2, y1, depth)) * 8) + 6))

file = "test_sword.obj"
with open(file, "w") as file:
    for v in real_vertices:
        file.write("v {} {} {}\n".format(*v))
    for f in faces:
        file.write("f {} {} {} {}\n".format(*f))
