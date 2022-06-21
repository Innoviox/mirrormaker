vertices = []

with open("test_sword.txt") as f:
    for x, line in enumerate(f):
        for y, ch in enumerate(line):
            if ch in '123456789':
                vertices.append((x, y))  # int(ch)))

real_vertices = []
faces = []
for v in vertices:
    # each vertex gets a square around it
    x, y = v
    sq = [(x, y, 0), (x + 1, y, 0), (x, y + 1, 0), (x + 1, y + 1, 0)]  # todo z

    l = len(real_vertices)
    faces.append((l + 1, l + 2, l + 4, l + 3))
    # faces.append((l + 1, l + 2, l + 3))
    # faces.append((l + 2, l + 3, l + 4))

    real_vertices.extend(sq)

file = "test_sword.obj"
with open(file, "w") as file:
    for v in real_vertices:
        file.write("v {} {} {}\n".format(*v))
    for f in faces:
        file.write("f {} {} {} {}\n".format(*f))
