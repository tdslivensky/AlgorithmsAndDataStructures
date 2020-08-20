# python3
import sys

class Vertex:
    def __init__(self, symbol):
        self.next = []
        self.patternEnd = False
        self.symbol = symbol

def Solve(text, n, patterns):
    result = []
    trie = BuildTrie(patterns)
    t = text
    count = 0
    while len(t) != 0:
        curr = Match(t, trie)
        if curr == True:
            result.append(count)
        count += 1
        t = t[1:]
    return result

def BuildTrie(patterns):
    trie = []
    currentVertex = Vertex('root')
    trie.append(currentVertex)
    count = 0

    for p in patterns:
        index = 0
        currentVertex = trie[0]
        eva = False
        for i in range(len(p)):
            currentSymbol = p[i]
            for n in currentVertex.next:
                if currentSymbol == trie[n].symbol:
                    index = n
                    currentVertex = trie[index]
                    eva = True
                    if (i+1) == len(p):
                        trie[index].patternEnd = True
            if eva == False:
                count += 1
                add = Vertex(currentSymbol)
                trie.append(add)
                trie[index].next.append(count)
                index = count
                currentVertex = trie[count]
            eva = False
        trie[count].patternEnd = True
    return trie

def Match(text, trie):
    index = 0
    currentSymbol = text[index]
    currentNode = trie[index]
    a = 0 
    eva = False
    while a < len(text):
        for n in currentNode.next:
            if currentSymbol == trie[n].symbol:
                if len(trie[n].next) == 0 or trie[n].patternEnd == True:
                    return True
                else:
                    index += 1
                    currentNode = trie[n]
                    currentSymbol = "-1" if len(text) == index else text[index]
                    eva = True
                    break
        if eva == False:
            return False
        a += 1
        eva = False
    return False





text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = Solve(text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')

# text = 'ATTGTTTTCTCGAGCGC'
# n = 7
# patterns = ['TAATA', 'AAGTGAGCAG','GCTCACATA', 'CCAC', 'C','GCC','TGTTCTTA']

# text = 'AAA'
# n = 1 
# patterns = ['AA']

# text = 'ACATA'
# n = 3 
# patterns = ['AT', 'A', 'AG']

# text = 'AATCGGGTTCAATCGGGGT'
# n = 2
# patterns = ['ATCG', 'GGGT']

# ans = Solve(text, n, patterns)

# sys.stdout.write (' '.join (map (str, ans)) + '\n')
