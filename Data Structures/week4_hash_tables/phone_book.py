# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]
    # q  = ['add 911 police', 'add 76213 Mom', 'add 17239 Bob', 'find 76213', 'find 910', 'find 911', 'del 910', 'del 911', 'find 911', 'find 76213', 'add 76213 daddy', 'find 76213']
    # n = 12
    # q = ['find 3839442', 'add 123456 me', 'add 0 granny', 'find 0', 'find 123456', 'del 0', 'del 0', 'find 0']
    # n = 8
    # return [Query(q[i].split()) for i in range(n)]
    

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # create array with 0 at every point possible
    A = [0]*10000000
    for q in queries:
        #if add make that index point the name
        if q.type == 'add':
            A[q.number] = q.name
        # if del make that index point 0
        elif q.type == 'del':
            A[q.number] = 0
        # otherwise check the index point for a name or 0
        else:
            if A[q.number] == 0:
                result.append('not found')
            else:
                result.append(A[q.number])
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

