#Uses python3

import sys

# similar solution but only one loop
def negative_cycle(adj, cost):
    #write your code here
    dist=[float('inf')]*len(adj)
    dist[0] = 0
    #goes through every vertex including the last (|V|) cycle
    for i in range(len(adj)):
        if dist[i] == float('inf'):
            dist[i] = 0
        # relax all edges |V| times but there is an added check on the |V|th trip
        for u in range(len(adj)):
            if dist[u] == float('inf'):
                dist[u] = 0
            for v in adj[u]:
                #see below for option w/o this .index function
                v_index = adj[u].index(v)
                if dist[v] > dist[u] + cost[u][v_index]:
                    dist[v] = dist[u] + cost[u][v_index]
                    # on the |V| trip if you do a relaxation then you have a cycle
                    if i == len(adj) - 1:
                        return 1
    return 0

# similar solution but only one loop and fastest solution at 2.59s
def negative_cycle2(adj, cost):
    #write your code here
    dist=[float('inf')]*len(adj)
    dist[0] = 0
    #goes through every vertex including the last (|V|) cycle
    for i in range(len(adj)):
        if dist[i] == float('inf'):
            dist[i] = 0
        # relax all edges |V| times but there is an added check on the |V|th trip
        for u in range(len(adj)):
            if dist[u] == float('inf'):
                dist[u] = 0
            for v in range(len(adj[u])):
                #v_index = adj[u].index(v)
                if dist[adj[u][v]] > dist[u] + cost[u][v]:
                    dist[adj[u][v]] = dist[u] + cost[u][v]
                    # on the |V| trip if you do a relaxation then you have a cycle
                    if i == len(adj) - 1:
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
    print(negative_cycle2(adj, cost))

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     data = [4, 4, 1, 2, -5, 4, 1, 2, 2, 3, 2, 3, 1, 1] #1
#     data = [5, 5, 1, 2, 1, 5, 1, 2, 2, 3, 2, 3, 4, -5, 4, 2, 1]
#     data = [10, 9, 1, 2, 1, 5, 6, 1, 6, 7, 1, 8, 9, 1, 9, 10, 1, 3, 4, 1, 7, 8, 1, 4, 5, 1, 2, 3, 1] #0
#     data = [5, 7, 1, 2, 4, 1, 3, 3, 2, 3, -2, 3, 4, -3, 4, 2, 4, 4, 5, 2, 3, 5, 1] # 1
#     data = [2, 2, 1, 2, 1, 2, 1, 3] #0
#     data = [2, 2, 1, 2, -1, 2, 1, 3] #0
#     data = [2, 2, 1, 2, -1, 2, 1, -1] #1
#     data = [7, 7, 1, 2, -1, 2, 3, -1, 3, 4, -1, 4, 1, 1, 5, 6, 1, 6, 7, 1, 7, 5, 1] #1
#     data = [7, 7, 1, 2, 1, 2, 3, 1, 3, 4, 1, 4, 1, 1, 5, 6, -1, 6, 7, -1, 7, 5, 1] #1
#     data = [6, 11, 1, 6, -10, 1, 2, 3, 2, 6, 8, 2, 3, 3, 2, 5, -5, 3, 5, 1, 3, 6, 3, 3, 4, 2, 5, 4, 0, 6, 5, 5, 6, 2, 2] #0
#     data = [6, 11, 1, 2, -10, 1, 3, 3, 2, 3, 2, 3, 2, 8, 2, 4, 5, 3, 4, -5, 3, 5, 3, 5, 4, 1, 5, 2, 3, 5, 6, 2, 4, 6, 0] #0
#     data = [6, 9, 1, 3, 1, 1, 5, 1, 5, 3, 1, 4, 1, 1, 3, 4, 1, 4, 6, 1, 3, 2, -5, 2, 6, 1, 6, 3, 1] # 1
#     data = [6, 7, 1, 2, 2, 2, 3, 3, 3, 1, 1, 4, 2, 3, 5, 4, 1, 4, 6, -2, 6, 5, -5] #1
#     data = [4,  3, 1,  2, -1, 2,  3, -2, 3,  4, -3] #0
#     data = [5, 5, 1, 2, 1, 3, 1, 1, 3, 4, -1, 4, 5, -1, 5, 3, -1] #1
#     n, m = data[0:2]
#     data = data[2:]
#     edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
#     data = data[3 * m:]
#     adj = [[] for _ in range(n)]
#     cost = [[] for _ in range(n)]
#     for ((a, b), w) in edges:
#         adj[a - 1].append(b - 1)
#         cost[a - 1].append(w)
#     print(negative_cycle2(adj, cost))   