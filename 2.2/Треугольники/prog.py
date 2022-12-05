import itertools
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


def ccw(A, B, C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])


def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def matrix_copy(matrix: list) -> list:
    return [elem[:] for elem in matrix]


def _line_equation(c1, c2, c3):
    if (c1[0] == c2[0] and c1[0] == c3[0]) or (c1[1] == c2[1] and c1[1] == c3[1]):
        return True
    try:
        y = (c3[1]-c1[1])/(c2[1]-c1[1])
        x = (c3[0]-c1[0])/(c2[0]-c1[0])
    except ZeroDivisionError:
        return False
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


with open('plist.txt', 'r') as f:
    f = f.readline().strip()
    f = f.split("]")[:-2]
    f = list(map(lambda a: a[1:], f))
    f = list(set(map(lambda a: tuple(map(int, a.split(','))), f)))


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


counter = 0
list_of_fourangles = []
print(f)
for item in itertools.combinations(f, 4):
    cordinates1 = item[0]
    cordinates2 = item[1]
    cordinates3 = item[2]
    cordinates4 = item[3]
    # if (5, 0) in item and (50, 8) in item and (50, 46) in item:
    #     logging.debug(
    #         f"1   {cordinates1},{cordinates2},{cordinates3},{cordinates4}")
    if intersect(cordinates1, cordinates4, cordinates3, cordinates2):
        cordinates4, cordinates3 = cordinates3, cordinates4
    if intersect(cordinates1, cordinates2, cordinates3, cordinates4):
        cordinates2, cordinates3 = cordinates3, cordinates2
    if not _line_equation_four([cordinates1, cordinates2, cordinates3, cordinates4]):
        counter += 1
        list_of_fourangles.append(
            Fourangle([cordinates1, cordinates2, cordinates3, cordinates4]))

print(max(list_of_fourangles))
print(min(list_of_fourangles))
