#Tim's 'encryption'
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

def encrypt(text):
    result = ""
    s = ''
    while (len(s) < 2 * len(text)):
        s += str(generateS())
    s = s[0:2 * len(text)]

    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) + int(s[2*i:2*i+2]) - 32) % 95 + 32)
    return result

def fileEncrypt(inF,outF):
    for lines in inF:
        lines = lines.strip()
        print(encrypt(lines),file=outF)

def main():
    inF = loadInFile(input('Unincrypted Doc: '))
    outF = loadOutFile(input('New file name for encrypted doc: '))
    key = input('Key: ')
    random.seed(key)
    fileEncrypt(inF,outF)

main()
                       

