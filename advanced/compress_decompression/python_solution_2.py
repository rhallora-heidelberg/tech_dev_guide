from collections import deque
import sys

def decompress(text):
    i = 0
    tDeque = deque()

    while i < len(text):
        if text[i] is "[":
            i += 1
            tDeque.append("[")
        elif text[i] is "]":
            i += 1
            collapse(tDeque)
        elif text[i].isdigit():
            firstDigitInSequence = i
            i += 1
            while i < len(text) and text[i].isdigit():
                i += 1
            tDeque.append(int(text[firstDigitInSequence:i]))
        else: #valid input assumed, must be character
            firstCharInSequence = i
            i += 1
            while i < len(text) and text[i].islower():
                i += 1
            tDeque.append(text[firstCharInSequence:i])
  
    for string in tDeque: #iterates as a queue here, not a stack
        sys.stdout.write(string)
    sys.stdout.write("\n")

def collapse(tDeque):
    chars = ""

    while tDeque[-1] is not "[":
        chars = tDeque.pop() + chars
    else:
        tDeque.pop()
        if chars is not "":
            #Could check for values >1 here, if there is a reason to expect that often
            if isinstance(tDeque[-1], int):
                chars *= tDeque.pop()
            tDeque.append(chars)


if __name__ == '__main__':
    decompress(sys.argv[1])