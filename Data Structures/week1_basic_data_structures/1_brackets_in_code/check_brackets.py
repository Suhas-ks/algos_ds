# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


# def are_matching(left, right):
#     return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((i, next))
        elif next in ')]}' and opening_brackets_stack != []:
            ind, top = opening_brackets_stack.pop()
            if top + next in ["()", "[]", "{}"]:
                continue
            elif top != next:
                return i + 1
        elif next in ')]}' and opening_brackets_stack == []:
            return i + 1
    if opening_brackets_stack != []:
        return opening_brackets_stack[0][0] + 1
    else:
        return "Success"


def main():
    text = input()
    # text = '12462{}{()}}}][][)()'
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
