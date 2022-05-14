from cmath import inf
import copy
import math


class graph_Matrix():
    def __init__(self, list1):
        self.matrix = []
        self.naming = list(map(lambda x: x.strip(), list1[0][1:]))
        for i in range(1, len(list1)):
            self.matrix.append(list(map(infadder, map(int, a[i][1:]))))

        self.setPath()

    def __str__(self):
        return self.outputMatrix(self.matrix)

    def __repr__(self):
        return self.outputMatrix(self.matrix)

    def setPath(self):
        self.path = []
        self.root = [[""]*len(self.matrix[0])
                     for n in range(len(self.matrix[0]))]
        self.path = copy.deepcopy(self.matrix)
        counter = 0
        while counter < len(self.path):
            for i in range(len(self.path)):
                for j in range(len(self.path[0])):
                    if (self.path[i][counter] != 0) and (self.path[counter][j] != 0):
                        if self.path[i][j] > self.path[i][counter]+self.path[counter][j]:
                            self.path[i][j] = self.path[i][counter] + \
                                self.path[counter][j]
                            self.root[i][j] = self.root[i][counter]+ self.naming[counter]
            counter += 1
        return self.outputMatrix(self.path)

    def outputMatrix(self, list1):
        output = "  "
        output += ", ".join(self.naming) + " \n"
        for i in range(len(list1)):
            output += str(self.naming[i])+" " + \
                str(list(map(zeroadder, list1[i])))[1:-1] + " \n"
        return output

    def editMatrix(self, param, i, j):
        self.matrix[i][j] = param
        self.setPath()

    def getPath(self, start, finish):
        counter = 0
        for i in range(len(self.naming)):
            if start == self.naming[i]:
                lineStart = i
                counter += 1
                continue
            elif finish == self.naming[i]:
                columnFinish = i
                counter += 1
                continue
        if counter != 2:
            print("Ошибка")
            return
        output = str(self.path[lineStart][columnFinish])
        if output == "0":
            output = str(
                min(filter(lambda x: (x != 0), self.path[columnFinish]))) + " reverse path"
        output += " "+start
        if self.root[lineStart][columnFinish] != "":
            output += str(self.root[lineStart][columnFinish])
        output += finish
        return output

# основан на алгоритме Флойда + парочка функций для интереса


def FileReaderMatrix(name):
    a = []
    f = open(name, "r").readlines()
    for line in f:
        a.append(list(line.split(" ")))
    return a


def zeroadder(name):
    name = str(name)
    if len(name) < 2:
        name = "0"+str(name)
    return name


def infadder(num):
    if num == 0:
        return math.inf
    return num


a = [[0, "A", "B", "C", "D"],
     ["A", 0,  1,  6,  0],
     ["B", 0,  0,  4,  1],
     ["C", 0,  0,  0,  0],
     ["D", 0, 0,  1,  0]]
a = FileReaderMatrix("input.txt")
print("\n")
graph = graph_Matrix(a)
# graph.edit_Matrix(3,1,0)
print(graph)
print(graph.setPath())
print(graph.getPath(input("введите точку начала: "), input("введите точку конца: ")))
