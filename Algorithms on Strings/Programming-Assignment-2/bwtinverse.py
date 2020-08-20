# python3
import sys

def InverseBWT(bwt):
    count = {}
    bwtCounts = []
    for i in range(len(bwt)):
        letter = bwt[i]
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
        bwtCounts.append((letter, count[letter]))

    bwtSorted = sorted(bwtCounts)
    key = {}
    
    for j in range(len(bwtSorted)):
        k = bwtSorted[j][0] + str(bwtSorted[j][1])
        v = bwtCounts[j][0] + str(bwtCounts[j][1])
        key[k] = v
    
    # index = 0
    # loops = 0
    # final = ""
    # while loops < len(bwtCounts):
    #     final = bwtSorted[index][0] + final
    #     endValue = bwtCounts[index]
    #     index = FindIndex(bwtSorted,endValue)
    #     loops += 1
    index = list(key.keys())[0]
    loops = 0
    final = "$"
    while loops < len(key)-1:
        endValue = key[index]
        final = endValue[0] + final
        index = endValue
        loops += 1

    return final

def FindIndex(l, tup):
    for i in range(len(l)):
        if l[i][0] == tup[0] and l[i][1] == tup[1]:
            return i

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))

# if __name__ == '__main__':
#     bwt = 'smnpbnnaaaaa$a'
#     bwt = 'AC$A'
#     bwt = 'AGGGAA$'
#     bwt = 'TTCCTAACG$A'
#     print(InverseBWT(bwt))