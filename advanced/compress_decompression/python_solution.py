from collections import deque
import sys

def decompress(text):
    tDeque = deque()

    for token in decompToTokens(text):
        #tDeque is treated as a stack here
        if token is "[":
            tDeque.append(token)
        elif token is "]":
            collapse(tDeque)
        elif isinstance(token, int):
            tDeque.append(token)
        else: #token is character/character sequence
            tDeque.append(token)

    for string in tDeque: #iterates as a queue here, not a stack
        sys.stdout.write(string)
    sys.stdout.write("\n")

def decompToTokens(text):
    i = 0

    while i < len(text):
        if text[i] is "[":
            i += 1
            yield "["
        elif text[i] is "]":
            i += 1
            yield "]"
        elif text[i].isdigit():
            firstDigitInSequence = i
            i += 1
            while i < len(text) and text[i].isdigit():
                i += 1
            yield int(text[firstDigitInSequence:i])
        else: #valid input assumed, must be character
            firstCharInSequence = i
            i += 1
            while i < len(text) and text[i].islower():
                i += 1
            yield text[firstCharInSequence:i]
               
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