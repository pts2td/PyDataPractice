'''
hello
'''
print "hello world"

from collections import defaultdict

def get_counts(sequence):
    counts = defaultdict(int) #initialize vals to 0
    for x in sequence:
        counts[x] += 1
    return counts
    
def top_counts(count_dict, n):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
    
