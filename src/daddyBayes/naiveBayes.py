"""
I'm going to do this string by string. 

for training 



tokenize string add it to a dictionary with that graded thing

Word,Senti
"bitcoin sell spree",-1 >= set1 = { "bitcoin": 1,
                                      "sell" : 1,
                                      "spree" : 1
                                    }
thisdict.update({"year": 2020}) 
thisdict["year"] = 2018
x = thisdict.keys() 

nive bayes = oc of word / all words in trained cats
"""
from coalas import csvReader as c
import math
import re

def clean(text):
    text = str(text)
    text = re.sub('[^A-Za-z]+', ' ', text).lower().strip()
    return text

def tokenize(text):
    text = clean(text)
    text = text.split(" ")
    return text


def lemma(text):
    text = tokenize(text)
    text = [word for word in text if not word in stop_words]
    lemma = " ".join(text)
    lemma = lemma.lower()
    return lemma

def setup(dictCount):
    for i in dictCount:
      globals()[f'dict{i}'] = {}

def train(x_train,y_test): # Input,Output
    for i in range(len(x_train)):  

        temp = tokenize(x_train[i])
        if y_test[i] == "-1":
            for value in temp:
                if value in Neg: 
                    Neg[value] += 1
                else:
                    Neg[value] = 1
        if y_test[i] == "0":
            for value in temp:
                if value in Neu: 
                    Neu[value] += 1
                else:
                    Neu[value] = 1
        if y_test[i] == "1":
            for value in temp:
                if value in Pos: 
                    Pos[value] += 1
                else:
                    Pos[value] = 1

def concatenate(array):
    if len(array) == len(set(array)):
        tempDict = dict()
        for value in array: 
            tempDict[value] = 1
        return tempDict
    else: 
        tempDict = dict()
        for value in array: 
            if value in tempDict: 
                tempDict[value] +=1
            else: 
                tempDict[value] = 1
        return tempDict
    

def classifer(text):
    temp = tokenize(text)
    td = concatenate(temp)
    print(td)
    ng = checkNeg(td)
    nu = checkNeu(td)
    ps = checkPos(td)
    if ng > nu and ng > ps:
        return -1
    if nu > ng and nu > ps:
        return 0
    if ps > nu and ps > ng:
        return 1
    print(f'Neg: {ng}, Neu: {nu}, Pos: {ps}') 


def getTotal(dic):
    temp = 0
    for i in dic:
        temp += dic[i]
    print(f'{c.col.BLUE}{temp}{c.col.ENDC}')
    return temp

def checkNeg(dic):
    prob = []
    total = getTotal(dic) + getTotal(Neg)
    for i in dic:
        if i in Neg:
            p = dic[i]+Neg[i]
            prob.append(p)
        else: 
            prob.append(1)
    temp = []
    for i in prob: 
        x = i/total
        print(f'{c.col.FAIL}{x}{c.col.ENDC}')
        temp.append(x)

    if len(temp) == 1:
        return(temp[0])
    else: 
        return math.prod(temp)
def checkNeu(dic):
    prob = []
    total = getTotal(dic) + getTotal(Neu)
    for i in dic:
        if i in Neu:
            p = dic[i]+Neu[i]
            print(f'{c.col.CYAN}{p}{c.col.ENDC}')
            prob.append(p)
        else: 
            prob.append(1)
    temp = []
    
    for i in prob: 
        x = i/total
        temp.append(x)
    if len(temp) == 1:
        return(temp[0])
    else: 
        return math.prod(temp)
    return x

def checkPos(dic):
    prob = []
    total = getTotal(dic) + getTotal(Pos)
    for i in dic:
        if i in Pos:
            p = dic[i]+Pos[i]
            prob.append(p)
        else: 
            prob.append(1)
    temp = []
    for i in prob: 
        x = i/total
        temp.append(x)
    if len(temp) == 1:
        return(temp[0])
    else: 
        return math.prod(temp)
    return x





if __name__ == "__main__":
    c.importCSV("../../tests/lemma.csv")
    c.printHeaders()
    Neg = dict()
    Neu = dict()
    Pos = dict()
    test = "pee pee poo poo in my bum bum"
    test =tokenize(test)
    test1 = "bitcoin pump slump"
    train(c.lemma, c.trained)
    print(classifer(test1))



    
    # train(c.lemma, c.trained)
