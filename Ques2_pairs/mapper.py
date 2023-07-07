#!/usr/bin/env python3

import sys

for line in sys.stdin:
    transactions = line.strip().split()
    length = len(transactions)

    for i in range(0,length-2):
        for j in range(i+1, length-1):
            for k in range(j+1,length):
                transactions_pair = transactions[i]+"_"+transactions[j]+"_"+transactions[k]
                print(transactions_pair,'\t',1)
            