import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more random text")

with open("mydata.txt", encoding="utf-8") as myFile:
    lineNum = 1
    
    while True:
        line = myFile.readline()
        
        if not line:
            break
        numWords = []
        numWords = line.split()
        
        char = 0
        for i in line:
            for j in i:
                char+=1
        
        avrgNumber =  char/ len(numWords) 
        print("Line", lineNum, " : ", len(numWords), avrgNumber, line, end="")
        lineNum += 1