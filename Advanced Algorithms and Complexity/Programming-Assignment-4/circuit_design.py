# python3

#import for use later
import itertools
import sys
import threading

#increase recursion limit as in previous lessons 
sys.setrecursionlimit(10**6) # max depth
threading.stack_size(2**26) # may need to increase stack to 2**29

# default reads imput 
n, m = map(int, input().split())
clauses = [ list(map(int, input().split())) for i in range(m) ]

class Vertex:
    def __init__(self,u):
        self.index = u
        self.valueInCNF = -1
        self.outNeighbors = [] #outgoing edges (u => v)
        self.inNeighbors = [] #incomming edges (parent => u)
        self.stronglyConnectedComponents = set() # a unique set of SCCs that a vertex is in
        self.rootOfSCC = False # it is the root of its scc
        # for trajan see links
        self.lowerVertex = -1 # smallest discovered vertex reachable from this one
        self.discoveryPoint = -1 # when it was discovered 
        self.onStack = False # is it on the stack 

# psuedo code 
# construct the implication graph G
# find SCC’s of G
# for all variables x:
    # if x and x lie in the same SCC of G:
        # return “unsatisfiable”
# find a topological ordering of SCC’s
# for all SCC’s C in reverse order:
    # if literals of C are not assigned yet:
        # set all of them to 1
        # set their negations to 0
# return the satisfying assignment


def isSatisfiable():
    graph = ConstructImplicationGraph(clauses)

    roots = Tarjans(graph)

    for vertex in roots:
        if -vertex in graph[vertex].stronglyConnectedComponents:
            return None
        # also check that compenents and their inverse aren;t in the SCC
        for literal in graph[vertex].stronglyConnectedComponents:
            if -literal in graph[vertex].stronglyConnectedComponents:
                return None
    # as roots contains the reverse topological order of the sccs, just go backwards and fill the values
    result = [0] * n
    for root in roots:
        for literal in graph[root].stronglyConnectedComponents:
            if graph[literal].valueInCNF == -1:
                graph[literal].valueInCNF = 1
                result[abs(literal) - 1] = literal
                graph[-literal].valueInCNF = 0
    return result


"""
this function constructs the needed implication graph from each u => v edge
returns a dicts of verticies {index: Vertex(index)}
remember edges are like a CNF clause so u => v
then 
not u implies v
v imples not u 
not v implies u 
and u imples not v 
https://en.wikipedia.org/wiki/Implication_graph
"""
def ConstructImplicationGraph(edges):
    # empty dict
    graph = {}
    #using 1 based verts and ensure we get reverse edges
    for i in range(1,n+1):
        graph[i] = Vertex(i)
        graph[-i] = Vertex(-i)
    for edge in edges:
        u = edge[0]
        # blank edge with no end/ circular edge
        if len(edge) == 1:
            graph[-u].outNeighbors.append(u)
            graph[u].inNeighbors.append(-u)
        #has beginning and end
        elif len(edge) == 2:
            v = edge[1]
            graph[-u].outNeighbors.append(v)
            graph[v].inNeighbors.append(-u)
            graph[-v].outNeighbors.append(u)
            graph[u].inNeighbors.append(-v)
    return graph

""" 
uses Tarjan's Algorithm to generate the SCCs. returns a list of roots in reverse topological order. 
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm 
has the code in the article
"""
def Tarjans(graph):
    index  = 0
    stack = []
    roots = []
    for vert in graph.keys():
        # we will use the function only if the vert has not been already found
        if graph[vert].discoveryPoint == -1:
            TarjanHelper(graph[vert], stack, index, graph, roots)
    return roots

def TarjanHelper(vertex, stack, index, graph, roots):
    vertex.discoveryPoint = index
    vertex.lowerVertex = index
    index += 1
    stack.append(vertex)
    vertex.onStack = True

    # DFS
    for outgoingVert in vertex.outNeighbors:
        if graph[outgoingVert].discoveryPoint == -1:
            # keep recurring when a vert has not been visited
            TarjanHelper(graph[outgoingVert], stack, index, graph, roots)
            vertex.lowerVertex = min(vertex.lowerVertex, graph[outgoingVert].lowerVertex)
        elif graph[outgoingVert].onStack == True:
            # the vertex is on the stack; back edge case
            # the outgoingVert is the root
            vertex.lowerVertex = min(vertex.lowerVertex, graph[outgoingVert].discoveryPoint)      

    #there is a SCC because there is a cycle
    if vertex.discoveryPoint == vertex.lowerVertex:
        # the stack now contains the cycle and a bunch of other verts 
        while len(stack) != 0:
            v = stack.pop()
            vertex.stronglyConnectedComponents.add(v.index)
            v.onStack = False
            # remove only until we reach the root 
            if v == vertex:
                break
        roots.append(vertex.index)


#added this for threadding issues

def main():
    result = isSatisfiable()
    if result is None:
       print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        #print(" ".join(str(-i-1 if result[i] else i+1) for i in range(n)))
        print(" ".join([str(i) for i in result]))


# This is to avoid stack overflow issues
threading.Thread(target=main).start()




# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.
# def isSatisfiable():
#     for mask in range(1<<n):
#         result = [ (mask >> i) & 1 for i in range(n) ]
#         formulaIsSatisfied = True
#         for clause in clauses:
#             clauseIsSatisfied = False
#             if result[abs(clause[0]) - 1] == (clause[0] < 0):
#                 clauseIsSatisfied = True
#             if result[abs(clause[1]) - 1] == (clause[1] < 0):
#                 clauseIsSatisfied = True
#             if not clauseIsSatisfied:
#                 formulaIsSatisfied = False
#                 break
#         if formulaIsSatisfied:
#             return result
#     return None


# def kosaraju(graph):
#     """ 
#     uses Kosaraju's Algorithm to generate the SCCs. returns a list of vertex roots of the SCCs. found thhis on internet. 
#     https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm
#     """
#     L = [] #list that stores traversals
#     explored = set()
#     # visit each vertex via dfs
#     for vertex in graph.keys():
#         visit(vertex, graph, explored, L)
#     # print(L)
#     # now assign values to root, forming SCCs
#     assigned = set()
#     roots = [] # stores roots of SCCs in topological order
#     for vertex in L:
#         assign(vertex, vertex, graph, assigned, roots)

#     # scc_roots_graph = { vertex : graph[vertex] for vertex in graph.keys() if graph[vertex].root }
#     # print({vertex : graph[vertex].scc for vertex in scc_roots_graph.keys()}, {vertex : graph[vertex].out_neighbors for vertex in graph.keys()})
#     # print(roots)
#     return roots

# def visit(u, graph, explored, L):
#     """
#     visits all vertices via dfs
#     prepends them to a list L (to keep v from appearing from u) for further processing
#     """
#     # print(explored, u, u not in explored)
#     # print()
#     if u not in explored:
#         explored.add(u)
#         L.insert(0, u)
#         for v in graph[u].out_neighbors:
#             # print(v, v not in explored, explored)
#             visit(v, graph, explored, L)

# def assign(u, root, graph, assigned, roots):
#     """ assigns all vertices to a SCC via dfs """
#     if u not in assigned:
#         graph[root].scc.add(u)
#         assigned.add(u)
#         if u == root:
#             graph[u].root = True
#             roots.append(u)
#         for v in graph[u].in_neighbors:
#             assign(v, root, graph, assigned, roots)