input_list = open("input.txt", "r")
n_vertex = [0 for i in range(int(input_list.readline()))]
edges = list(map(lambda s: s.strip(), input_list.readlines()))
for i in range(len(edges)):
    edges[i] = (tuple(map(lambda s: int(s), edges[i].split())))
for i in range(len(edges)):
    if n_vertex[edges[i][0]-1] != 0 and n_vertex[edges[i][1]-1] != 0 and (n_vertex[edges[i][0]-1] != n_vertex[edges[i][1]-1]):
        for h in range(n_vertex.count(x := max(n_vertex[edges[i][0]-1], n_vertex[edges[i][1]-1]))):
            n_vertex.insert(pos := n_vertex.index(x), min(
                n_vertex[edges[i][0]-1], n_vertex[edges[i][1]-1]))
            n_vertex.pop(pos+1)
        for h in range(len(n_vertex)):
            if n_vertex[h] > x:
                n_vertex[h] -= 1
    elif n_vertex[edges[i][0]-1] != 0:
        n_vertex[edges[i][1]-1] = n_vertex[edges[i][0]-1]
    elif n_vertex[edges[i][1]-1] != 0:
        n_vertex[edges[i][0]-1] = n_vertex[edges[i][1]-1]
    else:
        count_islands = max(n_vertex)+1
        n_vertex[edges[i][1]-1], n_vertex[edges[i]
                                          [0]-1] = count_islands, count_islands
count_islands = max(n_vertex)+1
for i in range(len(n_vertex)):
    if n_vertex[i] == 0:
        n_vertex[i] = count_islands
        count_islands += 1

print(max(n_vertex)-1)
