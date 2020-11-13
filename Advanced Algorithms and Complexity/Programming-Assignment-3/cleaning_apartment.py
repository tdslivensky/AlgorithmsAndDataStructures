# python3
import itertools

n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

clauses = []

#three possible colors
colors = range(1, 4)

#creates the list of literals for each possibility 
def exactly_one_of(itera):
    literals = []
    literals.append(' '.join(itera + ['0']))
    for i,j in itertools.combinations(itera, 2):
        literals.append('-{} -{} 0'.format(i,j))
    return literals

# transform array into input for sat solver
def inpt(l):
    l1 = []
    l1 = [[int(i) for i in (f[:-2].split(' '))] for f in l[1:]]
    #print(l1)
    return l1

def printEquisatisfiableSatFormula():
    listFormula = ['']
    dic = {}
    counter = 1
    bars = []

    # all nodes appear on path
    for vertex in range(1, n+1):
        for i in range(1,n+1):
            vert = str(vertex) * 2 + str(i)
            dic[vert] = counter
            counter += 1
            bars.append(str(dic[vert]))
    listFormula.append(' '.join(bars + ['0']))

    # ands a CNF for each vertex taking into account the fact that every vert can only be visited once
    for pos1, pos2 in itertools.combinations([p for p in range(1, n+1)], 2):
        for v in range(1, n+1):
            vv = str(v) * 2 + str(pos1)
            av = str(v) * 2 + str(pos2)
            listFormula.append('-{} -{} 0'.format(dic[vv], dic[av]))
    
    # add cnf for not vertex occupying the same position 
    for pos in range(1, n+1):
        samePosVerteices = [str(dic[str(v) * 2 + str(pos)]) for v in range(1, n+1)]
        listFormula += exactly_one_of(samePosVerteices)

    # add cnf for all vertex being connected 
    # CNF: (-xik V -xjk+1) if (k, k+1) not in E
    for vert1, vert2 in itertools.combinations([v for v in range(1, n+1)], 2):
        if [vert1, vert2] not in edges and [vert2, vert1] not in edges:
            for i in range(1, n):
                vv = str(vert1) * 2 + str(i)
                av = str(vert2) * 2 + str(i+1)
                listFormula.append('-{} -{} 0'.format(dic[vv], dic[av]))
                vv = str(vert1) * 2 + str(i+1)
                av = str(vert2) * 2 + str(i)
                listFormula.append('-{} -{} 0'.format(dic[vv], dic[av]))


    listFormula[0] = '{} {}'.format(len(listFormula)-1, len(dic))
    print('\n'.join(listFormula))   


# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
# def printEquisatisfiableSatFormula():
#     print("3 2")
#     print("1 2 0")
#     print("-1 -2 0")
#     print("1 -2 0")

printEquisatisfiableSatFormula()
