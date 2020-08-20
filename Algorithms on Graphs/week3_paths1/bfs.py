#Uses python3

import sys
import queue
from collections import deque

class Vertex():
    def __init__(self, edges):
        self.visited = False
        self.edges = edges
        self.distance = None

def Distance(adj, start, terminal):
    BreathFirstSearch(adj, start)
    if adj[terminal].distance == None:
        return -1
    else:
        return adj[terminal].distance

def BreathFirstSearch(graph, start):
    graph[start].distance = 0
    q = deque()
    q.append(graph[start])
    while len(q) != 0:
        currentVertx = q.popleft()
        for vertIndex in currentVertx.edges:
            if graph[vertIndex].distance == None:
                graph[vertIndex].distance = currentVertx.distance + 1
                q.append(graph[vertIndex])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [Vertex([]) for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].edges.append(b - 1)
        adj[b - 1].edges.append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(Distance(adj, s, t))

# if __name__ == '__main__':
#     #input = sys.stdin.read()
#     #data = list(map(int, input.split()))
#     #n, m = data[0:2]
#     #data = data[2:]
#     #edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
#     n, m = 4, 4
#     n, m = 5, 4
#     edges = [[1, 2], [4, 1], [2, 3], [3, 1]]
#     edges = [[5, 2], [1, 3], [3, 4], [1, 4]]
#     adj = [Vertex([]) for _ in range(n)]
#     for (a, b) in edges:
#         adj[a - 1].edges.append(b - 1)
#         adj[b - 1].edges.append(a - 1)
#     #s, t = data[2 * m] - 1, data[2 * m + 1] - 1
#     s, t = 2, 4
#     s, t = 3, 5
#     print(Distance(adj, s, t))
