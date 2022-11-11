from vectors import *


class Figure:
    def __init__(self, points):
        points_dict = []
        for i in points:
            points_dict.append({"x": i[0], "y": i[1]})
        self._pts = points_dict
        self._area = self._update_area()

    def _update_area(self):
        print("Fig::update_area")
        return 0

    @property
    def area(self):
        return self._area

    def __str__(self):
        return str(self._pts)+str(self._area)

    def __lt__(self, b):
        return self._area < b.area

    def __le__(self, b):
        return self._area <= b.area

    def __eq__(self, b):
        return self._area == b.area

    def __ne__(self, b):
        return self._area != b.area

    def __ge__(self, b):
        return self._area >= b.area

    def __gt__(self, b):
        return self._area > b.area


class Triangle(Figure):

    def _update_area(self):
        c = self._pts
        area = 0.5 * abs(((c[1]['x']-c[0]['x']) *
                          (c[2]['y']-c[0]['y']) -
                          (c[2]['x']-c[0]['x']) *
                          (c[1]['y']-c[0]['y'])))
        return area


class Fourangle(Figure):

    def _update_area(self):
        c = self._pts
        area = 0.5 * abs(((c[0]['x']-c[1]['x']) *
                          (c[0]['y']+c[1]['y']) +
                          (c[1]['x']-c[2]['x']) *
                          (c[1]['y']+c[2]['y']) +
                          (c[2]['x']-c[3]['x']) *
                          (c[2]['y']+c[3]['y']) +
                          (c[3]['x']-c[0]['x']) *
                          (c[3]['y']+c[0]['y'])))
        return area


def _line_equation(c1, c2, c3):
    try:
        y = (c3[1]-c1[1])/(c2[1]-c1[1])
        x = (c3[0]-c1[0])/(c2[0]-c1[0])
    except ZeroDivisionError:
        return True
    if y == x:
        return True
    return False


with open('plist.txt', 'r') as f:
    f = f.readline().strip()
    f = f.split("]")[:-2]
    f = list(map(lambda a: a[1:], f))
    # print(f)
    f = list(map(lambda a: tuple(map(int, a.split(','))), f))
    # print(f)
list_of_triangles = []

for cordinates1 in f:
    for cordinates2 in f:
        for cordinates3 in f:
            if cordinates1 != cordinates2 and cordinates1 != cordinates3 and cordinates3 != cordinates2:
                if not _line_equation(cordinates1, cordinates2, cordinates3):
                    list_of_triangles.append(
                        Triangle((cordinates1, cordinates2, cordinates3)))

print(max(list_of_triangles))
print(min(list_of_triangles))


for cordinates1 in f:
    for cordinates2 in f:
        for cordinates3 in f:
            for cordinates4 in f:
                pass

# print(dot_product([-3, -3], [-1, -3]))
# print(vector_lenght([-3, -3]), vector_lenght([-1, -3]))
# print(cos_of_vectors([3, 4], [4, 3]))
# print(angle_of_vectors([-3, -3], [3, 4]))
# print(angle_of_vectors([-3, -3], [-3, -1]))
# print(cos_of_vectors([-3, -3], [3, 3]))
# print(cos_of_vectors([-3, -3], [-3, -1]))

angles_f = []
center = 25
for i in range(len(f)):
    point = [f[i][0]-center, f[i][1]-center]
    angle = angle_of_vectors([-center, -center], point)
    if angle_of_vectors([-25, 25], f[i]) > 90:
        angle = 360-angle
    angles_f.append(angle)
sorted_f = [x for _, x in sorted(zip(angles_f, f), key=lambda pair: pair[0])]
print(sorted_f)
f = open("наборы.txt", 'w')
for i, cordinates1 in enumerate(sorted_f):
    for j, cordinates2 in enumerate(sorted_f[i+1:], i+1):
        for k, cordinates3 in enumerate(sorted_f[j+i+1:], j+i+1):
            for z, cordinates4 in enumerate(sorted_f[k+j+i:], k+i+j):
                if i == 0:
                    pass
                    f.write(' '.join(map(str, [cordinates1, cordinates2,
                            cordinates3, cordinates4]))+'\n')
f.close()
