import sys


alphabet = "abcdefghijklmnopqrstuvwxyz"
key = sys.argv[1]
keyList = []
for k in key:
    keyList.append(alphabet.index(k.lower()))
plaintext = input("plaintext: ")
ciphertext = ""
keyListCount = 0

for c in plaintext:
    if c.lower() not in alphabet:
        ciphertext = ciphertext + c
    else:
        newChar = ""
        indexAlph = alphabet.index(c.lower()) + keyList[keyListCount]
        if indexAlph >= 26:
            indexAlph = indexAlph - 26
        keyListCount = keyListCount + 1
        if keyListCount == len(keyList):
            keyListCount = 0
        if c.islower():
            newChar = alphabet[indexAlph]
            ciphertext = ciphertext + newChar
        else:
            newChar = alphabet[indexAlph].upper()
            ciphertext = ciphertext + newChar

print("ciphertext: " + ciphertext)