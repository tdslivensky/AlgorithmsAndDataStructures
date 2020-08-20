# python3
import random

def hash_func(pattern, prime, multiplier):
    #_multiplier = 263
    #_prime = 1000000007
    ans = 0
    for c in pattern:
        ans = (ans * multiplier + ord(c)) % prime
    return ans

def precomputeHAshes(Text, Pattern, prime, multiplier):
    # the dif of lengths
    dif = len(Text) - len(Pattern)
    # array of dif +1 length
    H = [0] * (dif + 1)
    # substring 
    S = Text[dif:len(Text) + 1]
    # innitialize the last value of the array
    H[dif] = hash_func(S, prime, multiplier)

    # compute x to the value of length of the pattern
    y = 1
    for i in range(1,len(Pattern)+1):
        y = (y*multiplier)%prime
    
    # itterate in reverse to fill out the array
    for i in range((dif - 1),-1,-1):
        a = Text[i+len(Pattern)]
        b = Text[i]
        # Z = Text[i:i+len(Pattern)]
        # hi = hash_func(Z, prime, multiplier)
        H[i] = (multiplier * H[i+1] + ord(b) - y*ord(a))%prime

    return H

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

# Naive general solution
def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]

# Naive Rabin Karp
def NaiveRabinKarp(T, Pattern):
    #big prime number
    p = 1000000007
    #random multiplier
    x = random.randrange(1, p-1)
    result = []
    patternHashVal = hash_func(Pattern,p,x)

    for i in range(len(T)-len(Pattern)):
        subEval = T[i:i+len(Pattern)-1]
        tHash = hash_func(subEval,p,x)
        if patternHashVal == tHash:
            if subEval == Pattern:
                result.append(i)
    return result

# Naive Rabin Karp
def RabinKarp(Pattern, Text):
    #big prime number
    p = 100000000007
    #random multiplier
    #x = random.randrange(1, p-1)
    x = 1
    result = []
    # hash of the pattern
    patternHashVal = hash_func(Pattern,p,x)
    # precompute the hash value of all the sub strings
    H = precomputeHAshes(Text,Pattern,p,x)
    
    #loop throught the range of possible substrings (substraction excludes the place where the substring could not be)
    for i in range(len(Text)-len(Pattern)+1):
        # if the patterns hash matches the precomputed hash
        if patternHashVal == H[i]:
            subEval = Text[i:i+len(Pattern)]
            # and the sub text matches the pattern
            if subEval == Pattern:
                # append start point
                result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
    # print_occurrences(RabinKarp('aba', 'abacaba'))
    # print_occurrences(RabinKarp('Test', 'testTesttesT'))
    # print_occurrences(RabinKarp('aaaaa', 'baaaaaaa'))
