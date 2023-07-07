#!/usr/bin/env python3

import sys



for line in sys.stdin:
    transactions = line.strip().split()
    length = len(transactions)

    for i in range(0,length):
        temp = []


        for j in range(i+1, length):
            temp.append(int(transactions[j]))
        print(transactions[i],'\t',temp)
            
