from vectors import *
import logging
logging.basicConfig(filename='log.log', filemode='w', level=logging.DEBUG)


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


def matrix_copy(matrix: list) -> list:
    return [elem[:] for elem in matrix]


def _line_equation(c1, c2, c3):
    try:
        y = (c3[1]-c1[1])/(c2[1]-c1[1])
        x = (c3[0]-c1[0])/(c2[0]-c1[0])
    except ZeroDivisionError:
        return True
    if y == x:
        return True
    return False


def _line_equation_four(points: list):
    for i in range(len(points)):
        copied_points = matrix_copy(points)
        copied_points.pop(i)
        if _line_equation(*copied_points):
            return True

    return False


def avarage_point(point, center, r_big, r_small):
    exp = (point[0]-center)**2+(point[1]-center)**2
    if exp < r_big**2 and exp > r_small**2:
        return False
    return True


with open('plist.txt', 'r') as f:
    f = f.readline().strip()
    f = f.split("]")[:-2]
    f = list(map(lambda a: a[1:], f))
    # print(f)
    f = list(map(lambda a: tuple(map(int, a.split(','))), f))
    # print(f)
# list_of_triangles = []

# for cordinates1 in f:
#     for cordinates2 in f:
#         for cordinates3 in f:
#             if cordinates1 != cordinates2 and cordinates1 != cordinates3 and cordinates3 != cordinates2:
#                 if not _line_equation(cordinates1, cordinates2, cordinates3):
#                     list_of_triangles.append(
#                         Triangle((cordinates1, cordinates2, cordinates3)))

# print(max(list_of_triangles))
# print(min(list_of_triangles))
# (12, 13), (21, 40), (38, 36), (37, 12)
# print(avarage_point((12, 13), 25, 15, 5))
# print(avarage_point((21, 40), 25, 15, 5))
# print(avarage_point((38, 36), 25, 15, 5))
# print(avarage_point((37, 12), 25, 15, 5))
# print(all([(lambda x: not avarage_point(x, 25, 15, 5))(x)
#       for x in [(12, 13), (21, 40), (38, 36), (37, 12)]]))
counter = 0
list_of_fourangles = []
# f = [(25, 25), (12, 13), (26, 36), (38, 36),
#      (27, 26), (20, 30), (37, 12), (21, 40)]
for cordinates1 in f:
    for cordinates2 in f:
        for cordinates3 in f:
            for cordinates4 in f:
                if all([cordinates1 not in [cordinates2, cordinates3, cordinates4], cordinates2 not in [cordinates3, cordinates4], [cordinates3 not in [cordinates4]]]):
                    if not _line_equation_four([cordinates1, cordinates2, cordinates3, cordinates4]):
                        if all([(lambda x: avarage_point(x, 25, 20, 5))(x) for x in [cordinates1, cordinates2, cordinates3, cordinates4]]):
                            counter += 1
                            # logging.debug(
                            #     f"{cordinates1}, {cordinates2}, {cordinates3}, {cordinates4}")

                            list_of_fourangles.append(
                                Fourangle([cordinates1, cordinates2, cordinates3, cordinates4]))
        logging.debug(f"{counter}")

print(max(list_of_fourangles))
# print(dot_product([-3, -3], [-1, -3]))
# print(vector_lenght([-3, -3]), vector_lenght([-1, -3]))
# print(cos_of_vectors([3, 4], [4, 3]))
# print(angle_of_vectors([-3, -3], [3, 4]))
# print(angle_of_vectors([-3, -3], [-3, -1]))
# print(cos_of_vectors([-3, -3], [3, 3]))
# print(cos_of_vectors([-3, -3], [-3, -1]))

# angles_f = []
# center = 25
# for i in range(len(f)):
#     point = [f[i][0]-center, f[i][1]-center]
#     angle = angle_of_vectors([-center, -center], point)
#     if angle_of_vectors([-25, 25], f[i]) > 90:
#         angle = 360-angle
#     angles_f.append(angle)
# sorted_f = [x for _, x in sorted(zip(angles_f, f), key=lambda pair: pair[0])]
# print(sorted_f)
# f = open("наборы.txt", 'w')
# for i, cordinates1 in enumerate(sorted_f):
#     for j, cordinates2 in enumerate(sorted_f[i+1:], i+1):
#         for k, cordinates3 in enumerate(sorted_f[j+i+1:], j+i+1):
#             for z, cordinates4 in enumerate(sorted_f[k+j+i:], k+i+j):
#                 if i == 0:
#                     pass
#                     f.write(' '.join(map(str, [cordinates1, cordinates2,
#                             cordinates3, cordinates4]))+'\n')
# f.close()
