from collections import defaultdict


class MirrorMaker:
    def __init__(self):
        self._vertices = []
        self.regions = {}
        self.vertices = []
        self.faces = []

    def find_vertices(self):
        self._vertices = []
        for x, line in enumerate(self.s):
            for y, ch in enumerate(line):
                if ch in '123456789':
                    self._vertices.append((x, y, int(ch)))

    def find_regions(self):
        self.regions = defaultdict(list)
        for x, line in enumerate(self.s):
            for y, char in enumerate(line):
                if char != '.':
                    start = (x, y)
                    # assume the region is right-rectangular (todo: unassume this)
                    # also assume the region never hits hte edge
                    a, b = x, y
                    while self.s[a][b] == char:
                        a += 1
                    a -= 1
                    while self.s[a][b] == char:
                        b += 1
                    b -= 1

                    if not any(r[1] == (a, b) for r in self.regions[int(char)]):
                        self.regions[int(char)].append((start, (a, b)))

    def _add_face(self, sq, face):
        l = len(self.vertices)
        self.faces.append([l + i for i in face])
        self.vertices.extend(sq)

    def load(self, file):
        self.s = open(file).read().split("\n")  # readlines adds spaces shut up

        self.find_vertices()
        self.find_regions()

        self.vertices = []
        self.faces = []

        for v in self._vertices:
            # each vertex gets a square around it
            x, y, depth = v

            for d in [depth, -depth]:
                sq = [(x, y, d), (x + 1, y, d), (x, y + 1, d),
                      (x + 1, y + 1, d)]  # todo z

                self._add_face(sq, (1, 2, 4, 3))

        for depth, region in self.regions.items():
            for r in region:
                topleft, bottomright = r
                x1, y1 = topleft
                x2, y2 = bottomright

                sq = [(x1, y1, depth), (x1, y2 + 1, depth),
                      (x1, y2 + 1, -depth), (x1, y1, -depth)]
                self._add_face(sq, [1, 2, 3, 4])
                # create top
                # faces.append(((vertices.index((x1, y1, depth)) * 8) + 1,
                #               (vertices.index((x1, y2, depth)) * 8) + 3,
                #               (vertices.index((x1, y2, depth)) * 8) + 7,
                #               (vertices.index((x1, y1, depth)) * 8) + 5))

                # create front
                # faces.append(((vertices.index((x1, y2, depth)) * 8) + 1,
                #               (vertices.index((x1, y2, depth)) * 8) + 5,
                #               (vertices.index((x2, y2, depth)) * 8) + 5,
                #               (vertices.index((x2, y2, depth)) * 8) + 1))

                # create back
                # faces.append(((vertices.index((x1, y1, depth)) * 8) + 1,
                #               (vertices.index((x1, y2, depth)) * 8) + 3,
                #               (vertices.index((x1, y2, depth)) * 8) + 7,
                #               (vertices.index((x1, y1, depth)) * 8) + 5))

                # create bottom
                # faces.append(((vertices.index((x2, y1, depth)) * 8) + 2,
                #               (vertices.index((x2, y2, depth)) * 8) + 4,
                #               (vertices.index((x2, y2, depth)) * 8) + 8,
                #               (vertices.index((x2, y1, depth)) * 8) + 6))

    def export(self, file="test_sword.obj"):
        with open(file, "w") as file:
            for v in self.vertices:
                file.write("v {} {} {}\n".format(*v))
            for f in self.faces:
                file.write("f {} {} {} {}\n".format(*f))


if __name__ == "__main__":
    mm = MirrorMaker()
    mm.load("test_sword.txt")
    mm.export()
