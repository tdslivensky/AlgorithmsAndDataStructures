# python3
import sys

def BWT(text):
    bwtMatrix = [text]

    for i in range(1,len(text)):
        prev = bwtMatrix[i-1]
        lastChar = prev[len(prev)-1]
        new = lastChar + prev[:len(prev)-1]
        bwtMatrix.append(new)

    bwtMatrix.sort()
    btw = ""
    for item in bwtMatrix:
        btw += item[len(item)-1]

    return btw
    #https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform

# if __name__ == '__main__':
#     text = sys.stdin.readline().strip()
#     print(BWT(text))

if __name__ == '__main__':
    text = 'AA$'
    text = 'ACACACAC$'
    text = 'AGACATA$'
    text = 'panamabananas$'
    print(BWT(text))