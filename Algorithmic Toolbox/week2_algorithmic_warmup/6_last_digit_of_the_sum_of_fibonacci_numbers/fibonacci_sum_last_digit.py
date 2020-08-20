# Uses python3
import sys

def fibonacciLastDigit(n):
    if n <= 1:
        return n

    current = 0
    next = 1

    for _ in range(n - 1):
        temp = next 
        next = (current + next) % 10 
        current  = temp

    return next

def FibLastDigit(n):
    return(fibonacciLastDigit((n+2) % 60))-1 % 10

def PisanoPeriod(m):
    current = 0 
    next = 1
    period = 0

    for _ in range(m*m):
        temp = next
        next = (current+next)%m
        current = temp
        period += 1
        if(current == 0 and next == 1):
            return period

# if __name__ == '__main__':
#     input = sys.stdin.read()100
n = int(input())
print(FibLastDigit(n))
