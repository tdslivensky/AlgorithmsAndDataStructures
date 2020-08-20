#Uses python3
import sys
import math

class Edge():
    def __init__(self, v1, v2, weight):
        self.start = v1
        self.end = v2
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

class Vertex():
    def __init__(self, id, x, y):
        self.id = id
        self.parent = id
        self.x = x
        self.y = y
        self.rank = 0
        self.edgesV = False



def MakeSet(x,y):
    s = []
    for i in range(len(x)):
        s.append(Vertex(i,x[i], y[i]))
    return s

def MakeEdges(s):
    edges = []
    for vertex in range(len(s)):
        s[vertex].edgesV = True
        for vertex2 in range(len(s)):
            if s[vertex].id != s[vertex2].id and s[vertex2].edgesV != True:
                w = DetermineWeight(s[vertex], s[vertex2])
                edges.append(Edge(s[vertex], s[vertex2], w))
    return edges

def DetermineWeight(start, end):
    x = start.x - end.x
    y = start.y - end.y
    r = math.sqrt((math.pow(x, 2) + math.pow(y,2)))
    return r

def Union(sets, v1, v2):
    p1 = Find(sets, v1)
    p2 = Find(sets, v2)
    Link(sets, sets[p1], sets[p2])

def Link(sets, v1, v2):
    if sets[v1.id].rank > sets[v2.id].rank:
        sets[v2.id].parent = v1.id
    else:
        sets[v1.id].parent = v2.id
        if v1.rank == v2.rank:
            v2.rank += 1

def Find(sets, v):
    if v.id != v.parent:
        sets[v.id].parent = Find(sets, sets[v.parent])
    return v.parent


def clustering(x, y, k):
    sets = MakeSet(x,y)
    edges = MakeEdges(sets)
    X = []
    edges.sort()
    for e in edges:
        a = Find(sets, e.start)
        b = Find(sets, e.end)
        if Find(sets, e.start) != Find(sets, e.end):
            X.append(e)
            Union(sets, sets[e.start.id], sets[e.end.id])
    
    f = X[len(x)-k].weight
    return f


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))

# if __name__ == '__main__':
#     data = [8, 3, 1, 1, 2, 4, 6, 9, 8, 9, 9, 8, 9, 3, 11, 4, 12, 4]
#     #data = [4, 0, 0, 0, 1, 1, 0, 1, 1, 2]
#     #data = [12, 7, 6, 4, 3, 5, 1, 1, 7, 2, 7, 5, 7, 3, 3, 7, 8, 2, 8, 4, 4, 6, 7, 2, 6, 3]
#     n = data[0]
#     data = data[1:]
#     x = data[0:2 * n:2]
#     y = data[1:2 * n:2]
#     data = data[2 * n:]
#     k = data[0]
#     print("{0:.9f}".format(clustering(x, y, k)))
