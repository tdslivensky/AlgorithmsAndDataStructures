#Uses python3

import sys
import math

def negative_cycle(adj, cost):
    # sets the dist for all nodes
    dist = [10**19] * len(adj)
    # define parent nodes
    prev = [-1] * len(adj)
    # defines the length it would take to get there
    length = [-1] * len(adj)

    # set all info of node zero so there are no inf comparisions at the start
    dist[0] = 0
    prev[0] = None
    length[0] = 0
    # for every node 
    for l in range(len(adj) - 1):
        # if it is a node we have never visted, we have disconnted node group and the root of that group needs to be set to 0
        if dist[l] == 10**19:
            dist[l] = 0
            prev[l] = None
            length[l] = 0
        #look at every edge
        for i in range(len(adj)):
            if dist[i] == 10**19:
                dist[i] = 0
                prev[i] = None
                length[i] = 0
            for j in range(len(adj[i])):
                # relax a node if there is a shorter distance to get there
                if dist[adj[i][j]] > dist[i] + cost[i][j]:
                    dist[adj[i][j]] = (dist[i] + cost[i][j])
                    prev[adj[i][j]] = i
                    length[adj[i][j]] = length[i] + 1
    #then do one final pass of the edges
    for k in range(len(adj)):   
        for vert in range(len(adj[k])):
            if dist[adj[k][vert]] > dist[k] + cost[k][vert]:
                # if you relax an edge again you must have a negative cycle
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))

# if __name__ == '__main__':
#     #input = sys.stdin.read()
#     #data = list(map(int, input.split()))
#     data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1] #1
#     data = [5, 5, 1, 2, 1, 5, 1, 2, 2, 3, 2, 3, 4, -5, 4, 2, 1]
#     data = [10, 9, 1, 2, 1, 5, 6, 1, 6, 7, 1, 8, 9, 1, 9, 10, 1, 3, 4, 1, 7, 8, 1, 4, 5, 1, 2, 3, 1] #0
#     data = [5, 7, 1, 2, 4, 1, 3, 3, 2, 3, -2, 3, 4, -3, 4, 2, 4, 4, 5, 2, 3, 5, 1] # 1
#     data = [2, 2, 1, 2, 1, 2, 1, 3] #0
#     data = [2, 2, 1, 2, -1, 2, 1, 3] #0
#     data = [2, 2, 1, 2, -1, 2, 1, -1] #1
#     data = [7, 7, 1, 2, -1, 2, 3, -1, 3, 4, -1, 4, 1, 1, 5, 6, 1, 6, 7, 1, 7, 5, 1] #1
#     data = [7, 7, 1, 2, 1, 2, 3, 1, 3, 4, 1, 4, 1, 1, 5, 6, -1, 6, 7, -1, 7, 5, 1] #1
#     #data = [6, 11, 1, 6, -10, 1, 2, 3, 2, 6, 8, 2, 3, 3, 2, 5, -5, 3, 5, 1, 3, 6, 3, 3, 4, 2, 5, 4, 0, 6, 5, 5, 6, 2, 2] #0
#     #data = [6, 11, 1, 2, -10, 1, 3, 3, 2, 3, 2, 3, 2, 8, 2, 4, 5, 3, 4, -5, 3, 5, 3, 5, 4, 1, 5, 2, 3, 5, 6, 2, 4, 6, 0] #0
#     #data = [6, 9, 1, 3, 1, 1, 5, 1, 5, 3, 1, 4, 1, 1, 3, 4, 1, 4, 6, 1, 3, 2, -5, 2, 6, 1, 6, 3, 1] # 1
#     #data = [6, 7, 1, 2, 2, 2, 3, 3, 3, 1, 1, 4, 2, 3, 5, 4, 1, 4, 6, -2, 6, 5, -5] #1
#     #data = [4,  3, 1,  2, -1, 2,  3, -2, 3,  4, -3] #0
#     #data = [5, 5, 1, 2, 1, 3, 1, 1, 3, 4, -1, 4, 5, -1, 5, 3, -1] #1
#     n, m = data[0:2]
#     data = data[2:]
#     edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
#     data = data[3 * m:]
#     adj = [[] for _ in range(n)]
#     cost = [[] for _ in range(n)]
#     for ((a, b), w) in edges:
#         adj[a - 1].append(b - 1)
#         cost[a - 1].append(w)
#     print(negative_cycle(adj, cost))    
