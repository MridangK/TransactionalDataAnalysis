#!/usr/bin/env python3
import sys
import os

absolute_path = os.path.abspath("Ques1_pair")

# Initialize variables
previous_pair = None
previous_pair_count = 0
transaction1_count = 0
current_pair = None


pair_file = open('Ques1_pair','r')

loaded_pairs = {}


for pair in pair_file:
    line = pair.strip().split('\t')
    item1 = line[0].strip()
    item2 = line[1].strip()
    count = int(line[2])
    loaded_pairs[item1+'_'+item2] = count

# Read input from standard input
for line in sys.stdin:
    # Strip whitespace from the line
    strip_line = line.strip()

    # Split the line into a transaction pair and its count
    current_pair,_ = strip_line.split('\t', 1)
    current_pair = current_pair.strip()

    # If the current pair is the same as the previous pair, increment the count
    if previous_pair == current_pair:
        previous_pair_count += 1
    else:
        # If the current pair is different from the previous pair, calculate and output the conditional probability
        if previous_pair:
            transaction1, transaction2,transaction3 = previous_pair.split('_')
            prob = previous_pair_count/loaded_pairs[transaction2+'_'+transaction3]
            print(transaction1, '\t', transaction2, '\t', transaction3, '\t', previous_pair_count, '\t', loaded_pairs[transaction2+'_'+transaction3], '\t', prob)
        # Reset the variables for the new pair
        previous_pair_count = 1
        previous_pair = current_pair

# Calculate and output the conditional probability for the last pair
transaction1, transaction2,transaction3 = previous_pair.split('_')
prob = previous_pair_count/loaded_pairs[transaction2+'_'+transaction3]
print(transaction1, '\t', transaction2, '\t', transaction3, '\t', previous_pair_count, '\t', loaded_pairs[transaction2+'_'+transaction3], '\t', prob)



