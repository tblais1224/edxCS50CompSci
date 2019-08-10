from nltk.tokenize import sent_tokenize


def lines(a, b):
    outputSet = set()
    aLines = a.split("\n")
    bLines = b.split("\n")
    for x in aLines:
        if x in bLines:
            outputSet.add(x.rstrip('\n'))
    # TODO
    return list(outputSet)


def sentences(a, b):
    outputSet = set()
    aSentences = sent_tokenize(a)
    bSentences = sent_tokenize(b)
    for x in aSentences:
        if x in bSentences:
            outputSet.add(x)
    # TODO
    return list(outputSet)


def substrings(a, b, n):
    outputSet = set()
    aList = []
    bList = []

    if n > len(a) or n > len(b):
        return outputSet

    for i in range(len(a) - (n - 1)):
        aList.append(a[i:i+n])
    for i in range(len(b) - (n - 1)):
        bList.append(b[i:i+n])

    if len(bList) >= len(aList):
        for i in bList:
            if i in aList:
                outputSet.add(i)
    else:
        for i in aList:
            if i in bList:
                outputSet.add(i)
    # TODO
    return list(outputSet)
