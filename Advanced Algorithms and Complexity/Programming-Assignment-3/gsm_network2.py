# python3
import itertools

n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

clauses = []

#three possible colors
colors = range(1, 4)

def varnum(i, k):
    #assert(i in digits and j in digits and k in digits)
    return 3*(i-1) + k


def exactly_one_of(itera):
    literals = []
    literals.append(' '.join(itera + ['0']))
    for i,j in itertools.combinations(itera, 2):
        literals.append('-{} -{} 0'.format(i,j))
    return literals

def inpt(l):
    l1 = []
    l1 = [[int(i) for i in (f[:-2].split(' '))] for f in l[1:]]
    print(l1)
    return l1

def printEquisatisfiableSatFormula():
    listFormula = ['']
    dic = {}
    counter = 1
    for vertex in range(1, n+1):
        bars = []
        #colors
        for i in range(1,4):
            vert = str(vertex) + str(i)
            dic[vert] = counter
            counter += 1
            bars.append(str(dic[vert]))
        listFormula += exactly_one_of(bars)
        
    # adj constraints
    for v1, v2 in edges:
        for i in range(1,4):
            b1 = str(v1) + str(i)
            b2 = str(v2) + str(i)
            listFormula.append('-{} -{} 0'.format(dic[b1], dic[b2]))
    listFormula[0] = '{} {}'.format(len(listFormula)-1, 3 * n)
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

# https://github.com/raunakchowdhury/cssi-coursera/blob/master/week03/gsm_network/gsm_network.py

