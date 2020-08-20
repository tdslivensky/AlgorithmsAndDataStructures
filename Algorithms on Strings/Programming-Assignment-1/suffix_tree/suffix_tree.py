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
  #t = text 
  s = BuildTrie(text)
  #s = suffixTrie
  #loops = 0
  index = 0
  result = []
  while index < len(s):
    if len(s[index].next) < 2 and s[index].delete == False:
      if len(s[index].next) == 1:
        s[index].end = s[s[index].next[0]].start
        s[s[index].next[0]].delete = True
        s[index].next = s[s[index].next[0]].next
      else:
        if s[index].start == s[index].end:
          result.append(text[s[index].start])
        elif s[index].end + 1 >= len(text):
          result.append(text[s[index].start:])
        else:
          result.append(text[s[index].start:s[index].end+1])
        index = index + 1
    else:
      index += 1

  # for vert in s:
  #   if vert.delete == False and vert.symbol != 'root':
  #     if vert.start == vert.end:
  #       result.append(text[vert.start])
  #     elif vert.end + 1 >= len(text):
  #       result.append(text[vert.start:])
  #     else:
  #       result.append(text[vert.start:vert.end+1])
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  
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