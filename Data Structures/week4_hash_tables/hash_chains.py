# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for _ in range(bucket_count)]

    # hash function
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    # input export stuff
    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    # actual code
    def process_query(self, query):
        # if check get all the values in the chain
        if query.type == "check":
            c = []
            # use reverse order, because we append strings to the end
            for t in reversed(self.elems[query.ind]):
                c.append(t)
            self.write_chain(c)    
        else:
            indE = self._hash_func(query.s)
            el = self.elems[indE]
            # if find go to the hash index and loop through the entries
            if query.type == 'find':
                found = False
                for t in el:
                    if t == query.s:
                        found = True
                        break
                self.write_search_result(found)
            # if adding check the hash index to see if already there and add if not
            elif query.type == 'add':
                found = False
                for t in el:
                    if t == query.s:
                        found = True
                        break
                if found == False:
                    el.append(query.s)
            else:
                # otherwise delete all instances of that word should only be one but just in case it check for mulitple 
                i = 0
                l = len(el)
                while i < l:
                    if self.elems[indE][i] == query.s:
                        self.elems[indE].pop(i)
                        l -= 1
                    else:
                        i += 1

    def process_queries(self):
        n = int(input())
        #n = 13
        #q = ['add world','add world', 'add HellO', 'check 4', 'find World', 'find world', 'del world', 'check 4', 'del HellO', 'add luck', 'add GooD', 'check 2', 'del good']
        #n = 8
        #q = ['add test', 'add test', 'find test', 'del test', 'find test', 'find Test', 'add Test', 'find Test']
        #n = 12
        #q = ['check 0','find help','add help','add del','add add','find add','find del','del del','find del','check 0','check 1','check 2']
        for i in range(n):
            self.process_query(self.read_query())
            #self.process_query(Query(q[i].split()))

if __name__ == '__main__':
    bucket_count = int(input())
    #bucket_count = 5
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
