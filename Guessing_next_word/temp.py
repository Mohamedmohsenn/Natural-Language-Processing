
from tkinter import * 

from nltk.corpus import PlaintextCorpusReader

path = "Khaleej-2004/Sports/"
corpusReader = PlaintextCorpusReader(path, ".*")
tokens = corpusReader.words()


def getCounterOfWords(userInput,tokens,dic) : 
    counter = 0
    myList = userInput.split(" ")
    
    for i in range (len(tokens)-2) : 
        if tokens[i] == myList[0] and tokens[i+1] == myList[1] :
            counter+=1
            if tokens[i+2] in dic :
                dic[tokens[i+2]]+=1
            else:
                dic[tokens[i+2]] = 1
                
    if tokens[(len(tokens))-2] == myList[0] and tokens[(len(tokens))-1] == myList[1]: 
        counter+=1
    return counter
    

def calculateProbability(dic,counter) :
    if counter != 0 :
        for key in dic :
            dic[key] /= counter
        
        
        
mp = {}
userInput = input()
counter = getCounterOfWords(userInput,tokens,mp)
calculateProbability(mp,counter)
sorted_dict = sorted(mp, key=mp.get , reverse=True) 
mn = min(len(sorted_dict),5)
for i in range(mn) :
    print(sorted_dict[i])
    
    
 
