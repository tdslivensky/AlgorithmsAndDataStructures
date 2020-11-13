# python3
import heapq
import math


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

class Vertex:
    def __init__(self, id, edges):
        self.id = id
        self.parent = None
        self.edges = edges
        self.distance = math.inf

    def __lt__(self, other):
        return self.distance < other.distance
# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [Vertex(i,[]) for i in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].edges.append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].edges.append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


# def read_data():
#     vertex_count, edge_count = map(int, input().split())
#     graph = FlowGraph(vertex_count)
#     for _ in range(edge_count):
#         u, v, capacity = map(int, input().split())
#         graph.add_edge(u - 1, v - 1, capacity)
#     return graph

def read_data():
    vertex_count, edge_count = 5, 7
    graph = FlowGraph(vertex_count)
    i = ['1 2 2', '2 5 5', '1 3 6', '3 4 2', '4 5 1', '3 2 3', '2 4 1']
    for j in range(edge_count):
        u, v, capacity = map(int, i[j].split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def max_flow(graph, from_, to):
    flow = 0
    p = Dijkstra(graph,from_, to)
    while len(p) != 0:
        mini = math.inf
        for edge in reversed(p):
            if mini > (graph.edges[edge].capacity - graph.edges[edge].flow):
                mini = (graph.edges[edge].capacity - graph.edges[edge].flow)
        
        for edge in reversed(p):
            graph.add_flow(edge, mini)

        flow += mini
        p = Dijkstra(graph,from_,to)   
    return flow

# dist between two nodes
def Dijkstra(graph, start, terminal):
    if len(graph.graph) == 1:
        return -1
    if start == terminal:
        return 0
    # make copy of graph to maintain updates
    eg = graph.graph.copy()
    eg[start].distance = 0
    tId = 0
    S = []
    while len(eg) != 0:
        # pop the lowest dist node
        curr = heapq.heappop(eg)
        S.append(curr)
        if curr.id == terminal:
            tId = len(S) - 1
        # look at its edges
        for edge in curr.edges:
            if (graph.edges[edge].capacity > graph.edges[edge].flow):
                #evalDist = (graph[curr.id].distance + edge.weight)
                #currDist = graph[edge.end].distance
                #graph.graph[graph.edges[edge].v]
                # if the distance at the end of the edge it greater than this new distance
                if graph.graph[graph.edges[edge].v].distance > (graph.graph[curr.id].distance + (graph.edges[edge].capacity - graph.edges[edge].flow)):
                    # update the dist and parent
                    graph.graph[graph.edges[edge].v].distance = (graph.graph[curr.id].distance + graph.edges[edge].capacity)
                    graph.graph[graph.edges[edge].v].parent = graph.graph[curr.id].id
                    # and put this new one on the heap. This cuases it to be pulled if needed and the heap to be up to date. But won't upset the og graph
                    heapq.heappush(eg, graph.graph[graph.edges[edge].v])
    
    # return the dist of the terminal node or -1
    result = True if graph.graph[terminal].distance != math.inf else False
    if result == True:
        path = []
        n = S[tId]
        while n.parent != None:
            p = graph.graph[n.parent]
            for edge in p.edges:
                if graph.edges[edge].v == n.id:
                    path.append(edge)
                    n = p
                    break
        return path
    else:
        return []

def InnitailizeSingleSource(graph, source):
    for vert in graph.graph:
        vert.distance = math.inf
        vert.parent = None
    
    graph[source].distance = 0


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
