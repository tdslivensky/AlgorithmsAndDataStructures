# Uses python3
import sys

def get_change(money):
    # innitialize dict
    Change = {0:0}
    # for c in range(1,money+1):
    #     Change[c] = c

    # coins
    coins = [1,3,4]

    # for values from 1 to money + 1
    for m in range(1,money+1):
        # add to dict if not there
        if m not in Change:
            Change[m] = m
        
        # for each coins
        for i in range(0,len(coins)):
            # if m (being the value up to money) > coins at i
            if m >= coins[i]:
                # coins to make change = previous change point (-1 -3 -4) + 1
                numCoins = Change[m-coins[i]] + 1
                # sets a minimum 
                if numCoins < Change[m]:
                    Change[m] = numCoins

    return Change[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m = 22,369,620
    print(get_change(m))
