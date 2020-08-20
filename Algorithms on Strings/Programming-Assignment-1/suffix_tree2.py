# python3
import sys

class Vertex:
    def __init__(self, symbol, start):
        self.next = []
        self.patternEnd = False
        self.start = start
        self.end = start
        self.symbol = symbol
        self.delete = False

def build_suffix_tree(text):
    trie = []
    currentVertex = Vertex('root',-1)
    trie.append(currentVertex)
    t = text
    count = 0
    loop = 0
    index = 0
    # currentVertex = Vertex(text, 0)
    # trie[0].next.append(1)
    # trie.append(currentVertex)
    result = []
    while len(t) != 0:
        #index = 0
        currentVertex = trie[0]
        eva = False
        for n in currentVertex.next:
            a = True
            tPrime = t
            parent = currentVertex.start
            while a == True:
                temp = trie[n].symbol[0]
                if temp == tPrime[0]:
                    temp = trie[n].symbol[1:]
                    trie[n].symbol = trie[n].symbol[0]
                    index += 1
                    trie[n].next.append(index)
                    trie.append(Vertex(temp, index))
                    parent = n
                    n = index
                    tPrime = tPrime[1:]
                    eva = True
                else:
                    if parent != -1:
                        index += 1
                        trie[parent].next.append(index)
                        trie.append(Vertex(tPrime, index))
                    a = False
        if eva == False:
            trie.append(Vertex(t, index))
            index += 1
            trie[0].next.append(index)
        t = t[1:]
  
  # Implement this function yourself
    return result
  #https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/suffixtrees.pdf

def BuildTrie(patterns):
    trie = []
    currentVertex = Vertex('root',-1)
    trie.append(currentVertex)
    t = patterns
    count = 0
    loop = 0
    while len(t) != 0:
        index = 0
        currentVertex = trie[0]
        eva = False
        for i in range(len(t)):
            currentSymbol = t[i]
            for n in currentVertex.next:
                if currentSymbol == trie[n].symbol:
                    index = n
                    currentVertex = trie[index]
                    eva = True
                    if (i+1) == len(t):
                        trie[index].patternEnd = True
            if eva == False:
                count += 1
                add = Vertex(currentSymbol, i + loop)
                trie.append(add)
                trie[index].next.append(count)
                index = count
                currentVertex = trie[count]
            eva = False
        trie[count].patternEnd = True
        t = t[1:]
        loop += 1
    return trie



# if __name__ == '__main__':
#   text = sys.stdin.readline().strip()
#   result = build_suffix_tree(text)
#   print("\n".join(result))

if __name__ == '__main__':
  text = 'ATAAATG$'
  result = build_suffix_tree(text)
  print("\n".join(result))