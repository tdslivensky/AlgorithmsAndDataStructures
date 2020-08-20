#Uses python3

import sys
import queue
import math
import heapq
class Vertex:
    def __init__(self, id):
        self.id = id
        self.visited = False
        self.edges = []
        self.parent = None
        self.distance = math.inf

    def __lt__(self, other):
        return self.distance < other.distance

class Edge:
    def __init__(self, end, wieght):
        self.end = end
        self.weight = wieght

# dist between two nodes
def distance(graph, cost, start, terminal):
    if len(graph) == 1:
        return -1
    if start == terminal:
        return 0
    # dist of start to 0
    graph[start].distance = 0
    # make copy of graph to maintain updates
    eg = graph.copy()
    # turn copy into heap to remove top value based on distance
    heapq.heapify(eg)

    while len(eg) != 0:
        # pop the lowest dist node
        curr = heapq.heappop(eg)
        #say we visted it
        graph[curr.id].visited = True
        # look at its edges
        for edge in curr.edges:
            #evalDist = (graph[curr.id].distance + edge.weight)
            #currDist = graph[edge.end].distance
            # if the distance at the end of the edge it greater than this new distance
            if graph[edge.end].distance > (graph[curr.id].distance + edge.weight):
                # update the dist and parent
                graph[edge.end].distance = (graph[curr.id].distance + edge.weight)
                graph[edge.end].parent = graph[curr.id].id
                # and put this new one on the heap. This cuases it to be pulled if needed and the heap to be up to date. But won't upset the og graph
                heapq.heappush(eg, graph[edge.end])
    
    # return the dist of the terminal node or -1
    result = graph[terminal].distance if graph[terminal].distance != math.inf else -1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [Vertex(i) for i in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].edges.append(Edge((b - 1),w))
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))

# if __name__ == '__main__':
#     # input = sys.stdin.read()
#     # data = list(map(int, input.split()))
#     # n, m = data[0:2]
#     # data = data[2:]
#     # edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
#     # data = data[3 * m:]
#     edges = [[[1, 2], 1], [[4, 1], 2], [[2, 3], 2], [[1, 3], 5]]
#     #edges = [[[1, 2], 1], [[1, 3], 1], [[2, 3], 1], [[3, 2], 1], [[2, 4], 1], [[3, 5], 1], [[5, 4], 1], [[2, 5], 1], [[3, 4], 1]]
#     #edges = [[[1, 2], 7], [[1, 3], 5], [[2, 3], 2]]
#     #edges =[[[1, 2], 1], [[2, 3], 2], [[1, 3], 5]]
#     #edges = []
#     n, m = 4, 4
#     #n, m = 5, 9
#     #n, m = 3, 3
#     #n, m = 4, 3
#     #n, m = 1, 0
#     adj = [Vertex(i) for i in range(n)]
#     cost = [[] for _ in range(n)]
#     for ((a, b), w) in edges:
#         adj[a - 1].edges.append(Edge((b - 1),w))
#         cost[a - 1].append(w)
#     # s, t = data[0] - 1, data[1] - 1
#     s, t = 0, 2
#     #s, t = 0, 0
#     #s, t = 0, 4
#     #s, t = 0, 2
#     print(distance(adj, cost, s, t))
