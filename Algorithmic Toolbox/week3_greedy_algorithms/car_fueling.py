# python3
import sys

# move along the path 
def compute_min_refills(distance, tank, stops):
    # write your code here
    numRefils = 0
    currentRefil = 0
    # this add a start at 0 and an end point to the array for simplicity
    stops.insert(0,0)
    stops.append(distance)

    # while we are have not reach the end
    while (currentRefil < len(stops) - 1):
        # the last refil point will be the update current refil
        lastRefil = currentRefil
        # currentrefil is then progressed till the maximal stop is found
        while (currentRefil < len(stops) - 1 and (stops[currentRefil + 1] - stops[lastRefil]) <= tank):
            currentRefil += 1
        # if no stop is found     
        if currentRefil == lastRefil:
            return -1
        # if a stop is found    
        if currentRefil < len(stops) - 1:
            numRefils += 1    
    return numRefils

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
