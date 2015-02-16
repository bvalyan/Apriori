'''
Created on Feb 11, 2015

@author: James Du
'''
from collections import Counter
from itertools import combinations

transactions = []
minsupct = 2;
numlines = 0;

#appends the input dataset file to the transactions table
def input(inFile):
    for line in inFile:
        lineSplit = line.split()
        transactions.append(lineSplit)
        global numlines
        numlines += 1
    inFile.close() 
    return transactions

#converts the items from the transactions table to a candidates itemset and support number
def convert_to_cand(transIDs):
    cand_listings = {}
    for items in transIDs:
        for indivItems in items:
            if indivItems in cand_listings:
                cand_listings[indivItems] += 1
            else:
                cand_listings[indivItems] = 1
    return cand_listings

#removes infrequent itemsets from candidates table and retains frequent itemsets in a new table
def convert_to_freq(candidates, minimum_support, line_count):
    freq_listings = {}
    for counter in candidates:
        if candidates[counter] >= minimum_support:
            freq_listings[counter] = candidates[counter];
    return freq_listings
    
def convert_to_cand2(frequent_listings, transIDs):
    cand_listings2 = {}
    for freqItem in frequent_listings:
        for freqItem2 in frequent_listings:
            if freqItem < freqItem2 and (freqItem, freqItem2) not in cand_listings2:
                cand_listings2[tuple([freqItem, freqItem2])] = 0
                for transItem in transIDs:
                    if freqItem in transItem and freqItem2 in transItem:
                        cand_listings2[freqItem, freqItem2] += 1
    return(cand_listings2)

def apriori (inputFile):
    inp = input(inputFile)
    cand = convert_to_cand(inp)
    freq = convert_to_freq(cand, minsupct, numlines)
    cand2 = convert_to_cand2(freq, inp)
    freq2 = convert_to_freq(cand2, minsupct, numlines)
    print(freq2)
    
apriori (open("C:\\Users\\Brandon\\workspace\\apriori2\\src\\data2.txt","r"))
