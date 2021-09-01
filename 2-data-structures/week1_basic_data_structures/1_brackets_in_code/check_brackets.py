# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text, 1):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
        if next in ")]}":
            if len(opening_brackets_stack) == 0: return i
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next): return i
    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[0].position
    else:
        return "Success"
    

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
