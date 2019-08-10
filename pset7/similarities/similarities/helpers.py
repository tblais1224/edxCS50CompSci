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
    aSubstrings = []
    bSubstrings = []

    for i in range(0, len(a), n):
        string = ""
        for k in range(0, n):
            if len(a) > i + k:
                string = string + a[i + k]
        aSubstrings.append(string)
    for i in range(0, len(b), n):
        string = ""
        for k in range(0, n):
            if len(b) > i + k:
                string = string + b[i + k]
        bSubstrings.append(string)

    for x in aSubstrings:
        if x in bSubstrings:
            outputSet.add(x)
    # TODO
    return list(outputSet)
