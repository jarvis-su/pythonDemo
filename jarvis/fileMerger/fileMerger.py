#!/usr/bin/python
import os
print("Hello, World!")

def compare(c1,c2):
    return (c1>c2)-(c1<c2)


def getValueFromSourceFile(key,value):
    sourceFilePath = "/Users/Jarvis/PycharmProjects/pythonDemo/testData/source"
    for srcFileName in os.listdir(sourceFilePath):
        srcFileFullName=os.path.join(sourceFilePath,srcFileName)
        print(srcFileFullName)
        for line in open(srcFileFullName):
            line=line.strip()
            if len(line)<=1:
                print("Empty line")
            elif line.startswith('#'):
                print("comments , ignore ")
            else:
                nPos=line.index('=')
                srcKey=line[0:nPos]
                if compare(key,srcKey)==0:
                    value=line[nPos+1:len(line)]
    return value





descFilePath="/Users/Jarvis/PycharmProjects/pythonDemo/testData/target"
descFiles=os.listdir(descFilePath)
for descFileName in descFiles:
    fullName=os.path.join(descFilePath,descFileName)
    print(fullName)

    for line in open(fullName):
        print(line)
        line=line.strip()
        print(len(line))
        if len(line)<=1:
            print("it's an empty line")
        elif line.startswith('#'):
            print("it's comments")
        else:
            print("it's key and value ")
            nPos=line.index('=')
            key=line[0:nPos]
            print(key)
            value=line[nPos+1:len(line)]
            newValue=getValueFromSourceFile(key,value)
            print("Old value is " + value)
            print("newValue is " + newValue)





