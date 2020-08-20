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

class FlowGraph:
    def __init__(self, n, f, c):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [Vertex(i,[]) for i in range(n)]
        self.flights = f
        self.crews = c

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
    
class MaxMatching:
    # def read_data(self):
    #     n, m = 2, 2
    #     inp = ['1 1', '1 0']
    #     n, m = 3, 4
    #     inp = ['1 1 0 1', '0 1 0 0', '0 0 0 0']
    #     adj_matrix = [list(map(int, inp[i].split())) for i in range(n)]
    #     flowGraph = self.CreateAdjacentList(adj_matrix, n, m)
    #     return flowGraph
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        flowGraph = self.CreateAdjacentList(adj_matrix, n, m)
        return flowGraph

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x) for x in matching]
        print(' '.join(line))

    def find_matching(self, flowGraph):
        l = max_flow(flowGraph, 0, len(flowGraph.graph)-1)
        return l

    def solve(self):
        FlowGraph = self.read_data()
        matching = self.find_matching(FlowGraph)
        self.write_response(matching)

    # puts the matrix into a flow graph cause it is easier for me to navigate
    def CreateAdjacentList(self,adjMatrix,n,m):
        totalNodes = n + m + 2
        adjList = FlowGraph(totalNodes, n, m)
        for i in range(1,n+1):
            adjList.add_edge(0,i,1)
        for i in range(n):
            for j in range(m):
                if adjMatrix[i][j] == 1:
                    adjList.add_edge(i+1,j+n+1,1)
        for i in range(m):
            adjList.add_edge(i+n+1, n+m+1, 1)
        return adjList    
    
def max_flow(graph, from_, to):
    #innitialize flow 
    flow = 0
    #determin the first path from start => end in reverse order
    FinalConnections = {}
    p = Path(graph,from_, to)
    for index in p:
        edg = graph.edges[index]
        if 0 < edg.u <= graph.flights:
            if index in FinalConnections:
                FinalConnections[index] = False
            else:
                FinalConnections[index] = True
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
        # --------------------------------------------------------------------------------------------------------------------------------------------------#
        # THIS IS THE CRITICAL DIFFERENCE IN THIS PROBLEM 
        #  once a path is determine we want to keep a running list of all the edges that connect pairs. 
        # to do this we use a dictionary FinalConnections with the key being the index value of the edge in the edge list
        for index in p:
            # edge to be determined
            edg = graph.edges[index]
            # make sure it is an edges that begins with a flight or crew or vice versa
            if 0 < edg.u <= (graph.flights + graph.crews) and 0 < edg.v <= (graph.flights + graph.crews):
                # when a backward facing edge's forward face partner is present int he dictionary. 
                if index-1 in FinalConnections:
                    # set the forward facing edge to false (ie. it is not actually a valid pair only a potential pair)
                    FinalConnections[index-1] = False
                else:
                    # otherwise add the edge to the dict
                    FinalConnections[index] = True
    # the final pairs are the array of len flights
    pairs = [-1] * graph.flights
    # for every key
    for key in FinalConnections:
        # if it is a valid edge pair
        if FinalConnections[key] == True:
            # set the flight's crew to the ending value of the edge minus the number of flights. 
            e = graph.edges[key]
            pairs[e.u - 1] = e.v - graph.flights
    # ------------------------------------------------------------------------------------------------------------------------------------------------------#
    return pairs

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
    max_matching = MaxMatching()
    max_matching.solve()

# https://www.youtube.com/watch?v=HTJjGw3HCBM 
# for inspiration on Hopcroft-Karp
