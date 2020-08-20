# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        # if the item is a bracket 
        if next in "([{":
            # if there is only a opening bracket
            if len(text) == 1:
                return 1
            # otherwise append a name tuple of that braket to stack
            opening_brackets_stack.append(Bracket(next,[next,i]))

        # if it is a closed bracket
        if next in ")]}":
            # and the stack is empty
            if len(opening_brackets_stack) == 0:
                return i + 1

            # get the last openign bracket    
            openingBracket = opening_brackets_stack[len(opening_brackets_stack)-1][0]
            closingBracket = next
            # if they matche
            if are_matching(openingBracket,closingBracket):
                #remove opener from stack
                opening_brackets_stack.pop()
            else:
                # if not i + 1
                return i+1
    # if the pass complete and stack is not empty             
    if len(opening_brackets_stack) != 0:
        # return the postiion of the item + 1
        return  opening_brackets_stack[len(opening_brackets_stack)-1][1][1] + 1
    else:
        # otherwise good
        return 'Success'


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    # text = '{}{}]'
    # mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
