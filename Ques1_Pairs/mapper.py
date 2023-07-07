#!/usr/bin/env python3

import sys

for line in sys.stdin:
    transactions = line.strip().split()
    length = len(transactions)

    for i in range(0,length-1):
        single_transaction = transactions[i]+"_$"
        print(single_transaction,'\t',1)
        for j in range(i+1, length):
            transactions_pair = transactions[i]+"_"+transactions[j]
            print(transactions_pair,'\t',1)
            
            
    single_transaction = transactions[length-1]+"_$"
    print(single_transaction,'\t',1)