# python3
import sys

# this function is used to limit the alphabet to only the needed chars 
# the other is $ as 0
def GetValue(char):
    if char == 'A':
        return 1
    elif char == 'C':
        return 2
    elif char == 'G':
        return 3
    elif char == 'T':
        return 4
    else:
        return 0

def build_suffix_array(text):
    #text += '$'
    order = SortCharacters(text)
    clas = ComputeClasses(text, order)
    l = 1
    # loop till your cyclic shift if going to be longer than the text
    while l < len(text):
        order = SortDoubled(text,l,order,clas)
        clas = UpdateClasses(order, clas, l)
        l = 2 * l
    
    return order

# this function sorts the initial string into into an ordered array with number representing the position of the letter in the string
# ie ababaa$ => [6,0,2,4,5,1,3] 
def SortCharacters(text):
    o = [-1] * len(text)
    c = [0] * 5
    # gets counts of amount of each value
    for i in range(len(text)):
        val = GetValue(text[i])
        c[val] = c[val] + 1
    for j in range(1,len(c)):
        val = c[j]
        c[j] = val + c[j-1]
    # goes in reverse to populate array
    for i in range(len(text)-1,-1, -1):
        val = GetValue(text[i])
        val2 = c[val] 
        c[val] = val2 - 1
        o[c[val]] = i
    
    return o

#creates classes for each letter
# ie ababaa$ => [6,0,2,4,5,1,3]  class => [1,2,1,2,1,1,0]
def ComputeClasses(text, order):
    cl = [0] * len(text)
    cl[order[0]] = 0

    for i in range(1, len(text)):
        if text[order[i]] != text[order[i-1]]:
            cl[order[i]] = cl[order[i-1]] + 1
        else:
            cl[order[i]] = cl[order[i-1]]
        
    return cl

# does a cyclic shift of Length L to create a new order 
# so ababaa$ => [6,0,2,4,5,1,3]  => $aaaabb
# becomes $a, a$, aa, ab, ab, ba, ba => [6,5,4,0,2,3,1] for L = 1
# becomes aa$a, baa$, abaa, a$ab, abab, baba, $aba => [4,3,2,5,0,1,6] which is ordered to [6,5,4,2,0,3,1] at the end L = 4

def SortDoubled(text,L,order,clas):
    count = [0] * len(text)
    newOrder = [0] * len(text)
    
    for i in range(len(text)):
        count[clas[i]] = count[clas[i]] + 1
    for j in range(1, len(text)):
        count[j] = count[j] + count[j-1]

    for i in range(len(text)-1,-1, -1):
        start = (order[i] - L + len(text))%len(text)
        cl = clas[start]
        count[cl] = count[cl] - 1
        newOrder[count[cl]] = start
    return newOrder

# simply updates the classes to match the new text components 
# $a, a$, aa, ab, ab, ba, ba => [6,5,4,0,2,3,1] for L = 1 starts with class => [1,2,1,2,1,1,0]
# the class comparisons are (0,1), (1,0), (1,1) ... (2,1)
# so functionally you compare (0,1) to (1,0) so it is a new class => [3,4,3,4,2,1,0]
def UpdateClasses(order, clas, L):
    n = len(order)
    newClass = [0] * n
    newClass[order[0]] = 0

    for i in range(1, n):
        # current order ex: 5
        cur = order[i]
        # prev order ex: 6
        prev = order[i-1]
        # starting position of the second halves 
        mid = (cur + L) % n #6
        midPrev = (prev + L) % n #0
        # if equivalen you are tin the same class if not the new class
        if clas[cur] != clas[prev] or clas[mid] != clas[midPrev]:
            newClass[cur] = newClass[prev] + 1
        else:
            newClass[cur] = newClass[prev]
    return newClass



if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))

# if __name__ == '__main__':
#     text = 'ATATAA$'
#     text = 'AAA$'
#     text = 'GAC$'
#     text = 'GAGAGAGA$'
#     text ='AACGATAGCGGTAGA$'
#     print(" ".join(map(str, build_suffix_array(text))))
