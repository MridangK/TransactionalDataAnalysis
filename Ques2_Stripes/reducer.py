#! /usr/bin/env python3

import sys


transaction_pair_count ={}

pair_file = open('Ques1_strips','r')

loaded_pairs = {}


for pair in pair_file:
    line = pair.strip().split('\t')
    item1 = line[0].strip()
    item2 = line[1].strip()
    count = int(line[3])
    loaded_pairs[item1+'_'+item2] = count

for line in sys.stdin:
    split_lie = line.strip()

    current_transaction, temp = split_lie.split('\t',1)

    temp = temp.strip()[1:-1].split(',')
    current_transaction = current_transaction.strip()

    for i in range(len(temp)):
        pair = current_transaction+'_'+str(temp[i].strip())
        if pair in transaction_pair_count:
            transaction_pair_count[pair]+=1
        else:
            transaction_pair_count[pair] = 1

for j in transaction_pair_count:
    count_total = transaction_pair_count[j]
    transaction1,transaction2,transaction3 = j.split('_')
    transaction1_count = loaded_pairs[transaction2+'_'+transaction3] 
    prob = count_total/transaction1_count
    print(transaction1, '\t',transaction2,'\t',transaction3,'\t',count_total,'\t',transaction1_count,'\t',prob)

