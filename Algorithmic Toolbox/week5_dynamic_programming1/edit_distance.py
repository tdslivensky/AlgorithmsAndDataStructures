# Uses python3
def edit_distance(s, t):
    A = [0] * (len(s)+1)
    # create a 2d matrix
    for k in range(len(A)):
        A[k] = ([0] * (len(t)+1))
        A[k][0] = k
    for k in range(len(t)+1):
        A[0][k] = k
    # add blanks    
    a = list(s)
    a.insert(0,'')
    b = list(t)
    b.insert(0,'')
    # for j in range 1 to len of second string ie the inner array ie rows
    # range 1 becasue we already handled 0 above
    for j in range(1,len(b)):
        # columns
        for i in range(1,len(a)):
            # calc all of the possible actions
            insertion = A[i][j-1] + 1
            deletion = A[i-1][j] + 1
            match = A[i-1][j-1]
            mismatch = match + 1
            # if the string match at this point use match 
            if a[i] == b[j]:
                A[i][j] = min(insertion,deletion,match)
            # else mismatch    
            else:
                A[i][j] = min(insertion, deletion, mismatch)
    # return the final distance
    return A[len(s)][len(t)]

if __name__ == "__main__":
    # a = 'editing'
    # b = 'distance'
    # print(edit_distance(a, b))
    print(edit_distance(input(), input()))
