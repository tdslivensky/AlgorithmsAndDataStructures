#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        # add max to stack
        self.maximum = None
        # stack of old maxes
        self.previousMaxes = []

    def Push(self, a):
        self.__stack.append(a)
        # when added if there is no max update
        if self.maximum == None:
            self.maximum = a
        # if it is greater put the old max in previous maxes and assign new max
        if a >= self.maximum:
            self.previousMaxes.append(self.maximum)
            self.maximum = a

    def Pop(self):
        assert(len(self.__stack))
        popped = self.__stack.pop()
        # if popped is the max and the stack if not empty
        if popped == self.maximum and len(self.__stack) != 0:
            # make last max the max
            lastMax = self.previousMaxes.pop()
            self.maximum = lastMax
            # if it was the last item there is no max
        elif len(self.__stack) == 0:
            self.maximum = None
        # else do nothing    
        else:
            self.maximum = self.maximum    

    def Max(self):
        assert(len(self.__stack))
        return self.maximum


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    # num_queries = 8
    # querries  = [['push', 2], ['push', 3], ['push', 9], ['push', 7], ['push', 2], ['max'], ['max'], ['max'], ['pop'], ['max']]
    # querries  = [['push', 1], ['push', 2], ['push', 9], ['max'], ['pop'], ['max'], ['pop'], ['max']]
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
