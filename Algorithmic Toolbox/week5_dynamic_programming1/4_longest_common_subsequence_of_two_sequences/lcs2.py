#Uses python3

import sys

def lcs2(a, b):
    if(len(a) == 0 or len(b) == 0):
        return 0
    final = [[],[]]
    EditDistanceMatrix = edit_distance(a,b)
    optimal_alignment(len(a)-1, len(b)-1, EditDistanceMatrix, final, a, b)
    count = 0
    for i in range(len(final[0])):
        if final[0][i] == final[1][i]:
            count += 1
    return count

def optimal_alignment(i,j, A, Final, s1, s2):
    if i == 0 and j == 0:
        return
    
    if i > 0 and A[i][j] == (A[i-1][j] + 1):
        optimal_alignment(i-1,j, A, Final, s1, s2)
        Final[0].append(s1[i])
        Final[1].append("-")
    elif j > 0 and A[i][j] == (A[i][j-1] + 1):
        optimal_alignment(i,j-1, A, Final, s1, s2)
        Final[0].append("-")
        Final[1].append(s2[j])
    else:
        optimal_alignment(i-1,j-1, A, Final, s1, s2)
        Final[0].append(s1[i])
        Final[1].append(s2[j])


def edit_distance(s, t):
    A = [0] * (len(s)+1)
    for k in range(len(A)):
        A[k] = ([0] * (len(t)+1))
        A[k][0] = k
    for k in range(len(t)+1):
        A[0][k] = k
    s.insert(0,'')
    t.insert(0,'')
    # for j in range 1 to len of second string ie the inner array ie rows
    # range 1 becasue we already handled 0 above
    for j in range(1,len(b)):
        # columns
        for i in range(1,len(a)):
            insertion = A[i][j-1] + 1
            deletion = A[i-1][j] + 1
            match = A[i-1][j-1]
            mismatch = match + 1
            if a[i] == b[j]:
                A[i][j] = min(insertion,deletion,match)
            else:
                A[i][j] = min(insertion, deletion, mismatch)

    return A

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
    # a = [2,7,5]
    # b = [2,5]
    # print(lcs2(a, b))
