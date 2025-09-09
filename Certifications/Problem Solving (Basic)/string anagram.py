#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    # Helper function to create a character frequency map for a string
    def get_char_map(s):
        char_map = {}
        for char in s:
            char_map[char] = char_map.get(char, 0) + 1
        return char_map
    
    # Create frequency maps for all dictionary strings
    dict_maps = [get_char_map(word) for word in dictionary]
    
    # Initialize result array
    result = []
    
    # For each query string
    for query_word in query:
        # Get its character frequency map
        query_map = get_char_map(query_word)
        count = 0
        
        # Compare with each dictionary word's frequency map
        for dict_map in dict_maps:
            # If maps are equal, they're anagrams
            if query_map == dict_map:
                count += 1
                
        result.append(count)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()