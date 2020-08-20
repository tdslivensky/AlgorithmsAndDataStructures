# Uses python3
import sys

def get_change(money):
    Change = {0:0}
    # for c in range(1,money+1):
    #     Change[c] = c
    coins = [1,3,4]

    for m in range(1,money+1):
        if m not in Change:
            Change[m] = m
        for i in range(0,len(coins)):
            if m >= coins[i]:
                numCoins = Change[m-coins[i]] + 1
                if numCoins < Change[m]:
                    Change[m] = numCoins

    return Change[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m = 22,369,620
    print(get_change(m))
