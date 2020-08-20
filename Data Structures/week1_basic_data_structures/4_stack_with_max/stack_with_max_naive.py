#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maximum = None
        self.previousMaxes = []

    def Push(self, a):
        self.__stack.append(a)
        if self.maximum == None:
            self.maximum = a
        if a >= self.maximum:
            self.previousMaxes.append(self.maximum)
            self.maximum = a

    def Pop(self):
        assert(len(self.__stack))
        popped = self.__stack.pop()
        if popped == self.maximum and len(self.__stack) != 0:
            lastMax = self.previousMaxes.pop()
            self.maximum = lastMax
        elif len(self.__stack) == 0:
            self.maximum = None
        else:
            self.maximum = self.maximum    

    def Max(self):
        assert(len(self.__stack))
        return self.maximum


if __name__ == '__main__':
    stack = StackWithMax()

    # num_queries = int(sys.stdin.readline())
    num_queries = 10
    querries  = [['push', 2], ['push', 3], ['push', 9], ['push', 7], ['push', 2], ['max'], ['max'], ['max'], ['pop'], ['max']]
    for i in range(num_queries):
        query = querries[i]

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
