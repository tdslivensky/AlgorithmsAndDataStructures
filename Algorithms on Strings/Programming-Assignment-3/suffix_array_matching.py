# python3
import sys

def find_occurrences(text, patterns):
    occs = set()

    # write your code here

    return occs

#https://stackoverflow.com/questions/49500809/find-all-occurrences-using-binary-search-in-a-suffix-array
#https://en.wikipedia.org/wiki/Suffix_array 
    

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))