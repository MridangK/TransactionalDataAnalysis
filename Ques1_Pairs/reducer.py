#!/usr/bin/env python3
import sys
# Initialize variables
previous_pair = None
previous_pair_count = 0
transaction1_count = 0
current_pair = None

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
            transaction1, transaction2 = previous_pair.split('_')
            if transaction2 == "$":
                transaction1_count = previous_pair_count
            else:
                prob = previous_pair_count/transaction1_count
                print(transaction1, '\t', transaction2, '\t', previous_pair_count, '\t', transaction1_count, '\t', prob)
        # Reset the variables for the new pair
        previous_pair_count = 1
        previous_pair = current_pair

# Calculate and output the conditional probability for the last pair
transaction1, transaction2 = previous_pair.split('_')
prob = previous_pair_count / transaction1_count
print(transaction1, '\t', transaction2, '\t', previous_pair_count, '\t', transaction1_count, '\t', prob)


