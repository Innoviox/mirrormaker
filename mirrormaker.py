vertices = []

with open("test_sword.txt") as f:
    for x, line in enumerate(f):
        for y, ch in enumerate(line):
            if ch in '123456789':
                vertices.append((x, y, int(ch)))

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

file = "test_sword.obj"
with open(file, "w") as file:
    for v in real_vertices:
        file.write("v {} {} {}\n".format(*v))
    for f in faces:
        file.write("f {} {} {} {}\n".format(*f))
