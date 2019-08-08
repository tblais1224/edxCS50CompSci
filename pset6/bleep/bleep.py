from cs50 import get_string
from sys import argv


def readBan():
    f = open(argv[1], "r")
    bannedSet = set()
    for word in f:
        word = word.rstrip('\n')
        bannedSet.add(word)
    return bannedSet


def addBleeps(text):
    banned = readBan()
    censoredText = ""
    words = text.split()
    for word in words:
        if word.lower() in banned:
            bleep = ""
            for c in word:
                bleep = bleep + "*"
            censoredText = censoredText + bleep + " "
        else:
            censoredText = censoredText + word + " "
    return censoredText


def main():
    if len(argv) != 2:
        exit(1)
    text = input("What message would you like to censor?\n")
    print(addBleeps(text))


main()