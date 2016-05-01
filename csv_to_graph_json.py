# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 11:33:52 2016

@author: Joy

Comments: not optimized for efficiency, rough test
          the "group" attribute of nodes will be used to color, for now preset to 1
"""

import string
import json

def main(filename):
    """takes a csv returns json prepped for graph layout"""
    fileData = open(filename, "r") 
    text = fileData.read()
    wordList = cleanList(text.split()) #returns list of clean words w/out stopwords
    
    nodes = createNodes(wordList)[0]

    print nodes

    links = createLinks(nodes, wordList)
    json_prep = {"nodes": nodes, "links":links}

    # Open a file for writing
    out_file = open("test1.json","w")
    
    # Save the dictionary into this file
    # (the 'indent=4' is optional, but makes it more readable)
    json.dump(json_prep,out_file, indent=4)          

def createLinks(nodes, wordList):
    linksValue = [] #will be list of links
    
    wordIndex = 0
    secondWordIndex = 0
    tempIndex = 0 #used to store secondWordIndex because it becomes wordIndex
    occurred = False
    #trying to build links, which takes source and destination
    # as indexes in the nodes list
 
    for listIndex in range(len(wordList)-1): #iterate through every word
        word = wordList[listIndex]
        secondWord = wordList[listIndex +1]
        
        for nodeIndex in range(len(nodes)): 
        #iterate through every unique word(node) to find index
            node = nodes[nodeIndex]
            nodeWord = node.get("text")
            
            # find first word index
            if(listIndex == 0):
                # first iteration needs to find first and second word, after that only second word
                if nodeWord == word:
                    wordIndex = nodeIndex
                    break

            else:
                wordIndex = tempIndex
                
            # find second word index
            if nodeWord == secondWord:
                tempIndex = secondWordIndex
                secondWordIndex = nodeIndex
                break
        #check if link has previosuly occurred
        for item in linksValue:
            if item.get("source") == wordIndex and item.get("target") == secondWordIndex:
                occurred = True
                item["occurances"] = item.get("occurances") + 1
        if occurred == False:
            temp = {"source": wordIndex, "target": secondWordIndex, "occurances": 1}
            linksValue.append(temp)  
        occurred = False
            
    return linksValue
        
def createNodes(words):
    """reads data returns nested dict with unique word as key and associated id as value"""

    nodesValue = []
    unique = []
       
    for word in words:
        if word in unique: 
            for obj in nodesValue:
                if obj["text"] == word:
                    obj["frequency"] += 1
        else:
            temp = {"text" : word, "group": 1, "frequency": 1}
            nodesValue.append(temp)
            unique.append(word)
            
    return nodesValue, unique

       
def cleanList(wordList):
    stopWordsData = open("stopwords.txt", "r")
    stopWords = stopWordsData.read()
    stopWords = stopWords.split()
    newWords = []
    
    for index in range(len(wordList)):
        word = wordList[index]
        word = clean(word)
        if word not in stopWords:
            newWords.append(word)
    
    return newWords
  
def clean(word):
    "cleans individual word"
    word = word.strip(string.punctuation + string.whitespace)
    word = word.lower()
    return word

main("honor_code.txt")

            