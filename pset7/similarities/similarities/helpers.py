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
    """Return sentences in both a and b"""

    # TODO
    return []


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    return []
