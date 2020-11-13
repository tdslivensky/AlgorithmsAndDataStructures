# python3

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column] or a[pivot_element.row][pivot_element.column] == 0:
        pivot_element.column += 1
    return pivot_element

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column

def ProcessPivotElement(a, b, pivot_element):
    # find the scale factor of the equation you are working on 
    scale_factor = a[pivot_element.row][pivot_element.column]
    #if your scale is not 1 then devide by you scal so it is 1 
    if scale_factor != 1:
        for i in range(len(a[pivot_element.row])):
            a[pivot_element.row][i] /= scale_factor
        b[pivot_element.row] /= scale_factor
    # for all equations in the matrix
    for i in range(len(a)):
        # if it is not the pivot
        if i != pivot_element.row:
            # only do subtracting when elements exist in the same col as pivot
            if a[i][pivot_element.column] != 0:
                #find the factor by which you want to multiply
                # if the factor is one that means we have reached the end and need to work backward 
                #example
                #[1 1 3] => [1 1 3] factor 2 => [1 0 2]
                #[2 3 7] => [0 1 1]          => [0 1 1]
                # after step two you have reduced it as far as possible
                # now your factor is 1 you don't need to multpy by a factor 
                # this way you zero out as you go for every var in every equation 
                factor = a[i][pivot_element.column] if a[i][pivot_element.column] != 1 else None
                if factor:
                    for col_index in range(len(a[i])):
                        a[i][col_index] -= factor * a[pivot_element.row][col_index]
                    b[i] -= factor * b[pivot_element.row]
                else:
                    for col_index in range(len(a[i])):
                        a[i][col_index] -= a[pivot_element.row][col_index]
                    b[i] -= b[pivot_element.row]

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
