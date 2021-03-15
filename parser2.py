#!/usr/bin/python
import re

def parser(inFile, outFile):
    output = open(outFile, "w+")
    output.write("facetNormalX,facetNormalY,facetNormalZ,Ver1X,Ver1Y,Ver1Z,Ver2X,Ver2Y,Ver2Z,Ver3X,Ver3Y,Ver3Z \n")
    
    fh = open(inFile, "r")
    block = ""
    
    #finds all numbers in scientific notation and put them into a list
    allVertices = re.findall(r"\b-?(\d*.\d*[eE].\d*)\b", fh.read())
    
    
    #debug
    #print(allVertices)
    
    #find number of times to run loop
    vertLength = len(allVertices)
    
    #debug
    #print(vertLength)
    count=0
    #loop vertLength number of times
    for i in range(0, vertLength):
        #debug
        # print(i)
        #print(allVertices[i])
        
        #add individual scinote num and a comma to a block
        block+=(allVertices[i]+",")
        count+=1
        
        #debug
        #print(block)
        
        #if there are 12 nums in the block, wtite it to the file and start a new block
       # if i != 0 and i%11 == 0:
        if count == 12:
            #print block without the last comma
            output.write(block[:-1]+"\n")
            #reset block for the next line
            block=""
            count=0

    output.close()
    
#test    
#parser("test2Input.stl", "output1.csv")

print("Enter input file name")
usrInp=(input())
print("Enter output file name")
usrOut=(input())
parser(usrInp, usrOut)