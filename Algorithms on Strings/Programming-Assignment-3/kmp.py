# python3
import sys

#the idea here is that you create a prefix array with the pattern first and then the text
# then if the prefix array is the same len as the pattern, that means that there was an occurance of the pattern
# this is because is hinges on the boarder matching principal

def find_pattern(pattern, text):
    #creates a full string so the pattern is the first border
    fullString = pattern + '$' + text
    #computes the prefix len array
    prefix = ComputePrefix(fullString)
    result = []
    # check to see if the len of pattern occures in the prefix array
    for i in range(len(pattern),len(fullString)):
        if prefix[i] == len(pattern):
            result.append(i-(2*len(pattern)))
    return result

def ComputePrefix(fullString):
    # make an array of len fullstring  
    s = [-1]*len(fullString)
    #innitialize 
    s[0] = 0
    # len of found border
    border = 0
    #in the full string
    for i in range(1,len(fullString)):
        #if there is a boarder going and it does not continue then backtrack till there is a match to this letter
        while border > 0 and fullString[i] != fullString[border]:
            border = s[border - 1]
        
        # if the border is growing add 1 or reset if not
        if fullString[i] == fullString[border]:
            border += 1
        else:
            border = 0
        s[i] = border

    return s


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))

# if __name__ == '__main__':
#     pattern = 'ATA'
#     text = 'ATATA'
#     pattern = 'ATAT'
#     text = 'GATATATGCATATACTT'
#     result = find_pattern(pattern, text)
#     print(" ".join(map(str, result)))

