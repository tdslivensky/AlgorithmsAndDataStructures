# python3

from collections import deque

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
        self.distance = None
    # comparison need for dijkstra but bfs works better than a djikstra weighting search not used in final
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

    # the below helper methods are not used
    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    # bit shifting is bullshit and isn't used 
    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

# def read_data():
#     vertex_count, edge_count = 5,7#4,5#5, 7
#     graph = FlowGraph(vertex_count)
#     i = ['1 2 2', '2 5 5', '1 3 6', '3 4 2', '4 5 1', '3 2 3', '2 4 1']
#     #i = ['1 2 10000', '1 3 10000', '2 3 1', '3 4 10000', '2 4 10000']
#     for j in range(edge_count):
#         u, v, capacity = map(int, i[j].split())
#         graph.add_edge(u - 1, v - 1, capacity)
#     return graph


def max_flow(graph, from_, to):
    #innitialize flow 
    flow = 0
    #determin the first path from start => end in reverse order
    p = Path(graph,from_, to)
    while len(p) != 0:
        #find the min value that can be added to flow
        minArray = []
        for edge in reversed(p):
            minArray.append(graph.edges[edge].capacity - graph.edges[edge].flow)
        mini = min(minArray)
        
        #for each eadge
        for edge in reversed(p):
            # if it is a forward edge then add to their flow and add capacity to the reverse so that you can move backwards if needed.
            if edge%2 == 0:
                graph.edges[edge].flow += mini
                graph.edges[edge+1].capacity += mini
            # otherwise it is a backwards edge in which case you add flwo to the reverse and remove flow from the forward
            else:
                graph.edges[edge].flow += mini
                graph.edges[edge - 1].flow -+ mini

        # add the new flow 
        flow += mini
        # find a new path
        p = Path(graph,from_,to)   
    return flow


def InnitailizeSingleSource(graph, source):
    # this is obvious 
    for vert in graph.graph:
        vert.distance = None
        vert.parent = None
    
    graph.graph[source].distance = 0
    graph.graph[source].parent = graph.graph[source].id

def BreathFirstSearch(graph,start, terminal):
    InnitailizeSingleSource(graph, start)
    # create a queue with only the start vertex
    q = deque()
    q.append(graph.graph[start])
    #standard BFS other than line 135
    while len(q) != 0:
        # pop the beginning of the queue
        currentVertex = q.popleft()
        for edgeIndex in currentVertex.edges:
            c = graph.edges[edgeIndex].capacity
            f =  graph.edges[edgeIndex].flow
            # KEY  DIIFERENCE ----------------------- FROM normal bfs. this skips edges with no availible capacity
            if graph.edges[edgeIndex].capacity > graph.edges[edgeIndex].flow:
                # this ensures you only update nodes not visited yet
                if graph.graph[graph.edges[edgeIndex].v].distance == None:
                    # if you are updating then update the distance from source & the parent
                    graph.graph[graph.edges[edgeIndex].v].distance = currentVertex.distance + 1
                    graph.graph[graph.edges[edgeIndex].v].parent = currentVertex.id
                    # don't bother adding the end node to the queue its a sink by necessity and therefore adds a pointless loop 
                    if (graph.graph[graph.edges[edgeIndex].v].id != terminal):
                        q.append(graph.graph[graph.edges[edgeIndex].v])

                        

def Path(graph,start,terminal):
    # run a bfs to determin shortest path
    BreathFirstSearch(graph,start,terminal)
    IsPath = True
    # if the end point was not reached then [] path
    if graph.graph[terminal].distance == None:
        IsPath = False
        return []
    if IsPath == True:
        Path = []
        #lastEdge = s[0][s[1]] 
        # work backward from the terminal to the beginning creating a possible path from edges that have availibel capacity. 
        n = graph.graph[terminal]
        while n.id != n.parent:
            p = graph.graph[n.parent]
            for edge in p.edges:
                # this if ensure that you don't get stuck in an infinite loop of the same path when mulitple edges point from one vertex to another. 
                if graph.edges[edge].v == n.id and graph.edges[edge].capacity > graph.edges[edge].flow:
                    Path.append(edge)
                    n = p
                    break
        #return the path
        return Path
    

if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))


# while dijkstra is a BFS algorithm it seems a bit over complicated for this problem. 
# ultimately D. hinges on the shortest path based on the weight of edges; however, wieght in this case in capacity - flow
# this becomes complicated. I ended up using the shorest path in number of segments not wieght. You could probably add a net weight (capacity - flow) 
# to the vertex as a self.netWeight and heappop off of that. you would have to get the lowest edges with capacity over 0 

# def Dijkstra(graph, start, terminal):
#     if len(graph.graph) == 1:
#         return -1
#     if start == terminal:
#         return 0
#     # make copy of graph to maintain updates
#     eg = graph.graph.copy()
#     eg[start].distance = 0
#     tId = 0
#     S = []
#     while len(eg) != 0:
#         # pop the lowest dist node
#         curr = heapq.heappop(eg)
#         S.append(curr)
#         if curr.id == terminal:
#             tId = len(S) - 1
#         # look at its edges
#         for edge in curr.edges:
#             if (graph.edges[edge].capacity > graph.edges[edge].flow):
#                 #evalDist = (graph[curr.id].distance + edge.weight)
#                 #currDist = graph[edge.end].distance
#                 #graph.graph[graph.edges[edge].v]
#                 # if the distance at the end of the edge it greater than this new distance
#                 if graph.graph[graph.edges[edge].v].distance > (graph.graph[curr.id].distance + (graph.edges[edge].capacity - graph.edges[edge].flow)):
#                     # update the dist and parent
#                     graph.graph[graph.edges[edge].v].distance = (graph.graph[curr.id].distance + graph.edges[edge].capacity)
#                     graph.graph[graph.edges[edge].v].parent = graph.graph[curr.id].id
#                     # and put this new one on the heap. This cuases it to be pulled if needed and the heap to be up to date. But won't upset the og graph
#                     heapq.heappush(eg, graph.graph[graph.edges[edge].v])
    
#     # return the dist of the terminal node or -1
#     result = True if graph.graph[terminal].distance != math.inf else False
#     if result == True:
#         path = []
#         n = S[tId]
#         while n.parent != None:
#             p = graph.graph[n.parent]
#             for edge in p.edges:
#                 if graph.edges[edge].v == n.id:
#                     path.append(edge)
#                     n = p
#                     break
#         return path
#     else:
#         return []