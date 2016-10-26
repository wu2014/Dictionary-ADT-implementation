"""
File: testBSTdict.py
test dictionary Implemented by binary search trees.
"""

import sys
import re
from time import clock
from BSTdict import BSTtreeDict



sys.setrecursionlimit(5000) 

fileNameOFStopWord = raw_input('Enter the filename of the stop words: ')
fileNameOfData = raw_input('Enter the filename of data file: ')
start = clock()
f = open(fileNameOFStopWord, 'r')
stop_words = BSTtreeDict()

lineNum = 0
for line in f:
    lineNum += 1 
    wordsInLine = re.findall(r"([A-Za-z]+(?!.*--)[A-Za-z-]*[A-Za-z']*)", line.strip())
    for word in wordsInLine:
        if not word.strip().lower() in stop_words:
            stop_words[word.strip().lower()] = [lineNum]
        else: 
            stop_words[word.strip().lower()] += [lineNum]   
        

f = open(fileNameOfData, 'r')
words = BSTtreeDict()

lineNum = 0
for line in f:
    lineNum += 1 
    wordsInLine = re.findall(r"([A-Za-z]+(?!.*--)[A-Za-z-]*[A-Za-z']*)", line.strip())
    for word in wordsInLine:
        word_lower = word.lower()
        if word_lower not in stop_words:
            if not word_lower in words:
                words[word_lower.strip()] = [lineNum]
            else:
                words[word_lower.strip()] += [lineNum]    
        
    
print "\nTree:\n" + str(words)
for item in words:
    print item +':'+ str(words[item])
end = clock()
runTime = end - start 
print "The time of dictionary using BST " + str(runTime)

