# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 20:26:24 2020

@author: shrey
"""

import pandas as pd
import time

filePath = input("Please provide the path of the file: ")
# filePath = 'db/dataA.csv'
# filePath = 'db/dataB.csv'
# filePath = 'db/dataC.csv'
# filePath = 'db/dataD.csv'
# filePath = 'db/dataE.csv'

start_time = time.time()

transactions = pd.read_csv(filePath, header=None, delimiter=',', engine='python', names=range(100))
transactions = transactions.where((pd.notnull(transactions)), None)

transactionItemMatrix = \
    pd.get_dummies(transactions.unstack().dropna()).groupby(level=1).sum()
transactionCnt, itemCnt = transactionItemMatrix.shape
print('The number of transactions in the dataset are: ',transactionCnt)
print('The number of different items in the dataset are: ',itemCnt,'\n')

largeItemsets = []
for items in range(1, itemCnt+1):
    from itertools import combinations
    for itemset in combinations(transactionItemMatrix, items):
        itemsetSupport = transactionItemMatrix[list(itemset)].all(axis=1).sum()
        s = [str(x) for x in itemset]
        if (len(s) >= 1):
            largeItemsets.append([",".join(s), itemsetSupport])
freqItemset = pd.DataFrame(largeItemsets, columns=["Itemset", "Support"])
results = freqItemset[freqItemset.Support >= 2]
print(results)


# dataFile = open('output.txt', 'w')

for eachitem in largeItemsets:
    dataFile.write(str(eachitem)+'\n')
dataFile.close()

print("--- %s seconds ---" % (time.time() - start_time))