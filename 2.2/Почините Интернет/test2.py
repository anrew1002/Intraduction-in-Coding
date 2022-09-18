input = open("input.txt", "r")
n_vertex = [0 for i in range(int(input.readline()))]
edges = list(map(lambda s: s.strip(), input.readlines()))
for i in range(len(edges)):
    edges[i] = (tuple(map(lambda s: int(s), edges[i].split())))
print(len(n_vertex)-len(edges)-1)
