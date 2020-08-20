# python3
import sys

# NA = -1

# class Node:
# 	def __init__ (self):
# 		self.next = [NA] * 4

def solve (text, n, patterns):
    result = []
    trie = BuildTrie(patterns)
    t = text
    count = 0

    while len(t) != 0:
        curr = Match(t, trie)
        if curr == True:
            result.append(count)
            count += 1
        else:
            count += 1
        
        t = t[1:]
    return result

def BuildTrie(patterns):
    trie = []
    currentNode = {}
    trie.append(currentNode)
    count = 0

    for p in patterns:
        index = 0
        currentNode = trie[0]
        
        for i in range(len(p)):
            currentSymbol = p[i]
            if currentSymbol in currentNode:
                index = currentNode[currentSymbol]
                currentNode = trie[index]
            else:
                add = {}
                count += 1
                trie.append(add)
                trie[index].update({currentSymbol: count})
                index = count
                currentNode = trie[count]
    
    return trie

def Match(text, trie):
    index = 0 
    currentSymbol = text[index]
    currentNode = trie[index]
    a = 0

    while a < len(text):
        if currentSymbol in currentNode:
            l = len(trie[currentNode[currentSymbol]])
            if l == 0:
                return True
            else:
                index += 1
                currentNode = trie[currentNode[currentSymbol]]
                currentSymbol = '-1' if len(text) == index else text[index]
        else:
            return False
        a += 1
    
    return False


text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')

# text = 'AATCGGGTTCAATCGGGGT'
# n = 2
# patterns = ['ATCG', 'GGGT']

# ans = solve (text, n, patterns)

# sys.stdout.write (' '.join (map (str, ans)) + '\n')
