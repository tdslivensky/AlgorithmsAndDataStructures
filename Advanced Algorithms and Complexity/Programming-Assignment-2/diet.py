# python3

#this works for bounded standard solutions (sometimes)
# further research needed for Big M method https://medium.com/@jacob.d.moore1/coding-the-simplex-algorithm-from-scratch-using-python-and-numpy-93e3813e6e70

from sys import stdin
import math
#N is the non basic vars 
#B is the basic vars 
#A is the matrix of coeffieints 
#b is the left side of Ax = b
#c is the maximization equation
#v is the contanst term of the optimization equation
#l is the leaving variable 
#e is the entering variable
#n is the number of constraints ie the num of basic variables
#m is the number of non basic variables
def Pivot(N, B, A, b, c, v, l, e):
    aHat = []
    for i in range(len(A)):
        aHat.append([])
        for j in range(len(A[0])):
            aHat[i].append(0)
    bHat = [0]*len(b)
    bHat[e] = b[l]/(A[l][e] *-1)
    # compute the coefiecients for the new basic variable e (ie Xe)
    for j in N:
        if j != e:
            aHat[e][j] = (A[l][j]) / (A[l][e] * -1)
    aHat[e][l] = 1/(A[l][e])
    # compute the coefficients of the remaining constraints
    for i in B:
        if i != l:
            bHat[i] = b[i] + ((A[i][e]) * bHat[e])
            for j in N:
                if j != e:
                    aHat[i][j] = A[i][j] + (A[i][e] * aHat[e][j])
            aHat[i][l] = (A[i][e] * aHat[e][l])
    # compute the objective function
    vHat = v + (c[e] * bHat[e])
    cHat = c.copy()
    for j in N:
        if j != e:
            cHat[j] = c[j] + (c[e] * aHat[e][j])
    cHat[l] = (c[e] * aHat[e][l])
    nHat = [l]
    BHat = [e]
    # compute the new basic varaibles 
    for n in N:
        if n != e:
            nHat.append(n)
    for b in B:
        if b != l:
            BHat.append(b)
    return nHat, BHat, aHat, bHat, cHat, vHat

def Simplex(n, m, A, b, c):
    feasible, N, B, A, b, c, v = InnitailizeSimplex(n, m, A, b, c)
    if feasible == False:
        return -1, []
    delta = [-1] * len(A)
    equationPositivity = DetermineIndexPositivity(N,c)
    while equationPositivity == True:
        #entering variable 
        e = FindEnteringIndex(N,c)
        for i in B:
            if A[i][e] * -1 > 0:
                delta[i] = b[i] / A[i][e] * -1
            else:
                delta[i] = math.inf
        l = FindLeavingIndex(B,A,e)
        if delta[l] == math.inf:
            return 1, []
        else:
            N, B, A, b, c, v = Pivot(N, B, A, b, c, v, l, e)
        equationPositivity = DetermineIndexPositivity(N,c)
    result = []
    for k in range(m):
        if k in B:
            result.append(b[k])
        else:
            result.append(0)

    return 0, result 

def DetermineIndexPositivity(N,c):
    for n in N:
        if c[n] > 0:
            return True
    return False

def FindEnteringIndex(N,c):
    for n in N:
        if c[n] > 0:
            return n
    return -1

def FindLeavingIndex(B, A, e):
    coefficients = 0
    indexL = B[0]
    for l in B:
        if A[l][e] < 0:
            if A[l][e] < coefficients:
                coefficients = A[l][e]
                indexL = l
    return indexL

def InnitailizeSimplex(n, m, A, b, c):
    minIndex = 0
    for i in range(1, len(b)):
        if b[i] < b[minIndex]:
            minIndex = i
    if b[minIndex] >= 0:
        N = [i for i in range(n)]
        B = [i for i in range(n,n+m)]
        for i in range(m):
            A.append([])
            for j in range(len(A[0])):
                A[i+n].append(A[i][j] * -1)
        for i in range(len(A)):
            for j in range(m):
                A[i].append(0)
        for i in range(m):
            b.insert(0,0)
            c.append(0)
        return True, N, B, A, b, c, 0
        # infeasible
    # change A, b, c to add slack form    
    for constraint in A:
        constraint.append(-1)
    for i in range(m):
        A.append([])
        for j in range(len(A[0])):
            A[i+n].append(A[i][j] * -1)
    for i in range(len(A)):
        A[i].append(0)
        A[i].append(0)
        A[i].append(0)
    #cPrime = [0] * len(c)
    cPrime = c.copy()
    for i in range(len(c)):
        cPrime[i] = 0
    cPrime.append(-1)
    xNaught = len(cPrime)-1
    for i in range(m+1):
        b.insert(0,0)
        cPrime.append(0)
    #m += 1
    N = [i for i in range(n)]
    B = [i for i in range(n,m+n)]
    l = n + minIndex
    N, B, A, b, cPrime, v = Pivot(N, B, A, b, cPrime, 0, l, 0)
    delta = [-1] * len(A)
    equationPositivity = DetermineIndexPositivity(N,cPrime)
    while equationPositivity == True:
        #entering variable 
        e = FindEnteringIndex(N,cPrime)
        for i in B:
            if A[i][e] > 0:
                delta[i] = b[i] / A[i][e]
            else:
                delta[i] = math.inf
        l = FindLeavingIndex(B,A,e)
        if delta[l] == math.inf:
            return 1, []
        else:
            N, B, A, b, cPrime, v = Pivot(N, B, A, b, cPrime, v, l, e)
        equationPositivity = DetermineIndexPositivity(N,cPrime)
    if v == 0:
        if xNaught in B:
            for x in N:
                if A[0][x] != 0:
                    e = x
                    break
            N, B, A, b, cPrime, v = Pivot(N, B, A, b, cPrime, v, xNaught, e)
        for a in A:
            a.pop()
        return True, N, B, A, b, cPrime, 0
    else:
        return False, N, B, A, b, c, 0

# this function is replaced by the Simplex function above
def solve_diet_problem(n, m, A, b, c):  
    # Write your code here
    return False, False #[0, [0] * m]

# original stuff 
# n, m = list(map(int, stdin.readline().split()))
# A = []
# for i in range(n):
#   A += [list(map(int, stdin.readline().split()))]
# b = list(map(int, stdin.readline().split()))
# c = list(map(int, stdin.readline().split()))

# n, m = 3, 3
# A = [[1,1,3],[2,2,5],[4,1,2]]
# b = [30,24,36]
# c = [3,1,2]
# n,m = 3,2
# A = [[-1,-1],[1,0],[0,1]]
# b = [-1,2,2]
# c = [-1, 2]

# n,m = 2,2
# A = [[2,-1], [1, -5]]
# b = [2, -4]
# c = [2, -1]
# n,m = 1, 3
# A = [[0, 0, 1]]
# b = [3]
# c = [1,1,1]

# n,m = 2,2
# A = [[2, -1], [1, -5]]
# b = [2, -4]
# c = [2, -1]

n,m = 5, 5
A = [[-77, 71, 15, 49, -2],[77, -71, 37, 89, 95],[31, 88, 62, 16, -73],[38, -47, 6, -42, -68],[59, 79, 26, -18, -92]]
b = [14736, 32998, 7529, 4667, 27779]
c = [-87, 87, -43, 86, 13]
anst, ansx = Simplex(n,m,A,b,c) #solve_diet_problem(n, m, A, b, c)

if anst == -1:
  print("No solution")
if anst == 0:  
  print("Bounded solution")
  print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
  print("Infinity")
    
