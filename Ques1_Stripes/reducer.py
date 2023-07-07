#! /usr/bin/env python3

import sys

transaction1_counts = {}
transaction_pair_count ={}

for line in sys.stdin:
    split_lie = line.strip()

    current_transaction, temp = split_lie.split('\t',1)

    temp = temp.strip()[1:-1].split(',')
    current_transaction = current_transaction.strip()

    if current_transaction in transaction1_counts.keys():
        transaction1_counts[current_transaction]+=1
    else:
        transaction1_counts[current_transaction]=1

    for i in range(0,len(temp)):
        pair = current_transaction + '\t' + str(temp[i].strip())
        if pair in transaction_pair_count:
            transaction_pair_count[pair]+=1
        else:
            transaction_pair_count[pair] = 1

for j in transaction_pair_count:
    count = transaction_pair_count[j]
    transaction1 = j.split('\t')[0]
    transaction1_count = transaction1_counts[transaction1]
    prob = count/transaction1_count
    print(j, '\t','\t',count,'\t',transaction1_count,'\t',prob)

