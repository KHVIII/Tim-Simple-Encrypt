#Tim's decryption

import random

def loadInFile(filename):
    inF = open(filename,'r')
    return (inF)

def loadOutFile(filename):
    outF = open(filename,'w')
    return (outF)

def generateS ():
    tempS = random.randint(0,10000)
    return tempS

def decrypt(text):
    result = ''
    s = ''
    while (len(s) < 2 * len(text)):
        s += str(generateS())
    s = s[0:2 * len(text)]

    for i in range (len(text)):
        char = text[i]
        result += chr(126 - (126 - (ord(char)- int(s[2*i:2*i+2])))%95)
    return result

def fileDecrypt(inF,outF):
    for lines in inF:
        lines=lines.strip()
        print(decrypt(lines),file=outF)

def main():
    inF = loadInFile(input('Tim_Encrypted_File Name: '))
    outF = loadOutFile(input('New file name for decrypted doc: '));
    key = input('Key: ')
    random.seed(key)
    fileDecrypt(inF,outF)

main()
