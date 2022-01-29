import re

#open and read input file
with open("declaration.txt", 'r') as readFile:
    lines = readFile.readlines()

    #get every word in the txt file and don't consider capitalization
    words = re.findall('\w+', open('declaration.txt').read().lower())

    #assign words to dictionary, word as key and count as value
    wordDict = {}
    for word in words:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1
   
    #open and write sorted dictionary into output file, each word on a new line
    with open("words.txt", 'w') as writeFile:
        for element in sorted(wordDict.keys()):
            writeFile.write(element + ' ' + str(wordDict[element]) + '\n')
    
