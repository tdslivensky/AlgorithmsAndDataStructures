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


def exactly_one_of(i):
    # clauses.append([l for l in literals])

    # for pair in itertools.combinations(literals, 2):
    #     clauses.append([-l for l in pair])
    literals = [varnum(i, c) for c in colors]
    clauses.append([l for l in literals])
    #gets the opposite pairing is (x and y and z)(not x and not y)(not x and not z) etc.
    for pair in itertools.combinations(literals, 2):
        clauses.append([-1 for l in pair])

#add adjancys constraints
def adjacency(i,j):
    for k in colors:
        clauses.append([-varnum(i,j), - varnum(j,k)])

#add base constraints 
for i in range(1, n+1):
    exactly_one_of(i)

#add adj constriants 
for i,j in edges:
    adjacency(i,j)

print(len(clauses), n * 3)
for c in clauses:
    c.append(0)
    print(' '.join(map(str,c)))
# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
# def printEquisatisfiableSatFormula():
#     print("3 2")
#     print("1 2 0")
#     print("-1 -2 0")
#     print("1 -2 0")

# printEquisatisfiableSatFormula()



