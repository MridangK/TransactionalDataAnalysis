#!/usr/bin/env python3

import sys



for line in sys.stdin:
    transactions = line.strip().split()
    length = len(transactions)

    for i in range(0,length-2):
        for j in range(i+1, length-1):
            pair = str(transactions[i])+'_'+str(transactions[j])
            temp = []
            for k in range(j+1, length):
                temp.append(int(transactions[k]))
            print(pair, '\t',temp)
            
